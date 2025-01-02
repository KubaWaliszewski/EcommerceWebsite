from chat.models import Room


class CreateRoomUseCase:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def execute(self, uuid, client, url):
        self.room_repository.create(uuid=uuid, client=client, url=url)


class DeleteRoomUseCase:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def execute(self, uuid):
        room = self.room_repository.get_by_uuid(uuid)
        self.room_repository.delete(room)


class GetOrUpdateRoomUseCase:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def execute(self, uuid, user):
        room = self.room_repository.get_by_uuid(uuid)

        if room.status == Room.WAITING:
            room.status = Room.ACTIVE
            room.agent = user
            self.room_repository.save(room)
        return room
    

class GetRoomUseCase:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    async def execute(self, uuid):
        room = await self.room_repository.get_room(uuid)
        if not room:
            raise ValueError(f"Room with UUID {uuid} does not exist.")

        return room
    
    
class DisconnectFromRoomUseCase:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    async def execute(self, room_name, user):
        room = await self.room_repository.get_room(room_name)
        if user.is_staff:
            return
        room.status = Room.CLOSED
        await self.room_repository.save(room)
