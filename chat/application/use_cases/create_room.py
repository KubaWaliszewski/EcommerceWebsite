from chat.models import Room

class CreateRoomUseCase:
    def __init__(self, room_repository):
        self.room_repository = room_repository

    def execute(self, uuid, client, url):
        self.room_repository.create(uuid=uuid, client=client, url=url)