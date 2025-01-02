from django.utils.timesince import timesince
from chat.templatetags.chatextras import initials

class ReceiveMessageUseCase:
    def __init__(self, message_repository):
        self.message_repository = message_repository

    async def execute(self, room_name, sent_by, message, agent):
        new_message = await self.message_repository.create_message(
            room_name, sent_by, message, agent
        )
        return {
            'message': new_message.body,
            'name': sent_by,
            'agent': agent,
            'initials': initials(sent_by),
            'created_at': timesince(new_message.created_at),
        }
