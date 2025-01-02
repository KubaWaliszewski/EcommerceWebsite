from asgiref.sync import sync_to_async

class MessageRepository:
    @sync_to_async
    def create_message(self, room_name, sent_by, body, agent):
        from chat.models import Room, Message
        from account.infrastructure.orm.models import CustomUser

        room = Room.objects.get(uuid=room_name)
        message = Message.objects.create(body=body, sent_by=sent_by)

        if agent:
            message.created_by = CustomUser.objects.get(pk=agent)
            message.save()

        room.messages.add(message)
        return message
