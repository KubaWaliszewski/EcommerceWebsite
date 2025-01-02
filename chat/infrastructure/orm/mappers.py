from chat.domain.entities.message import Message
from chat.domain.entities.room import Room
from chat.models import Message as ORMMessage, Room as ORMRoom

class MessageMapper:
    @staticmethod
    def to_domain(orm_message):

        return Message(
            body=orm_message.body,
            sent_by=orm_message.sent_by,
            created_at=orm_message.created_at,
            created_by=orm_message.created_by
        )

    @staticmethod
    def to_orm(domain_message):
        return ORMMessage(
            body=domain_message.body,
            sent_by=domain_message.sent_by,
            created_by=domain_message.created_by
        )

class RoomMapper:
    @staticmethod
    def to_domain(orm_room):
        messages = [MessageMapper.to_domain(msg) for msg in orm_room.messages.all()]
        return Room(
            uuid=orm_room.uuid,
            client=orm_room.client,
            status=orm_room.status,
            url=orm_room.url,
            created_at=orm_room.created_at,
            agent=orm_room.agent,
            messages=messages
        )

    @staticmethod
    def to_orm(domain_room):
        orm_room, created = ORMRoom.objects.get_or_create(
            uuid=domain_room.uuid,
            defaults={
                "client": domain_room.client,
                "status": domain_room.status,
                "url": domain_room.url,
                "agent": domain_room.agent
            }
        )
        if not created:
            orm_room.client = domain_room.client
            orm_room.status = domain_room.status
            orm_room.url = domain_room.url
            orm_room.agent = domain_room.agent

        orm_room.save()
        return orm_room