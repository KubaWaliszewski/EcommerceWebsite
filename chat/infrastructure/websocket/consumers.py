import json
from channels.generic.websocket import AsyncWebsocketConsumer

from chat.infrastructure.repositories.room_repository import RoomRepository
from chat.infrastructure.repositories.message_repository import MessageRepository
from chat.application.use_cases.room_use_cases import GetRoomUseCase, DisconnectFromRoomUseCase
from chat.application.use_cases.message_use_cases import ReceiveMessageUseCase


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user = self.scope['user']

        # Initialize repositories and use cases
        room_repository = RoomRepository()
        get_room_use_case = GetRoomUseCase(room_repository)
        
        # Join room group
        self.room = await get_room_use_case.execute(self.room_name)
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

         # Inform user
        if self.user.is_staff:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'users_update',
                }
            )



    async def disconnect(self, close_code):
        room_repository = RoomRepository()
        disconnect_from_room_use_case = DisconnectFromRoomUseCase(room_repository)

        await disconnect_from_room_use_case.execute(self.room_name, self.user)

        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        if not self.user.is_staff:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'user_left',
                }
            )


    async def receive(self, text_data):
        # Receive message from WebSocket (front end)
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        message = text_data_json['message']
        name = text_data_json['name']
        agent = text_data_json.get('agent', '')

        message_repository = MessageRepository()
        receive_message_use_case = ReceiveMessageUseCase(message_repository)

        if message_type == 'message':
            new_message = await receive_message_use_case.execute(
                self.room_name, name, message, agent
            )

            # Send message to group / room
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': new_message['message'],
                    'name': new_message['name'],
                    'agent': new_message['agent'],
                    'initials': new_message['initials'],
                    'created_at': new_message['created_at'],
                }
            )
        # Send update to the room
        elif message_type == 'update':
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'writing_active',
                    'message': message,
                    'name': name,
                    'agent': agent,
                }
            )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    async def writing_active(self, event):
        await self.send(text_data=json.dumps(event))

    async def users_update(self, event):
        await self.send(text_data=json.dumps({'type': 'users_update'}))

    async def user_left(self, event):
        await self.send(text_data=json.dumps({'type': 'user_left'}))
    