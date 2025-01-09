from asgiref.sync import sync_to_async
from chat.models import Room as ORMRoom
from chat.infrastructure.orm.mappers import RoomMapper

   
class RoomRepository:
    def create(self, uuid, client, url):
        if ORMRoom.objects.filter(uuid=uuid).exists():
            raise ValueError("Room with this UUID already exists")
        orm_room = ORMRoom.objects.create(uuid=uuid, client=client, url=url)
        return RoomMapper.to_domain(orm_room)


    def get_all(self):
        orm_rooms = ORMRoom.objects.all()
        return [RoomMapper.to_domain(room) for room in orm_rooms]

    
    def get_by_uuid(self, uuid): 
        orm_room = self.get_room_base(uuid)
        
        return orm_room
        
    @sync_to_async
    def get_room(self, uuid):
        orm_room = self.get_room_base(uuid)
        return RoomMapper.to_domain(orm_room) if orm_room else None


    def get_room_base(self, uuid): 
        try:
            return ORMRoom.objects.get(uuid=uuid)
        except ORMRoom.DoesNotExist:
            return None

    def _save_room(self, room):
        orm_room = RoomMapper.to_orm(room)
        orm_room.save()

    def save(self, room):
        self._save_room(room)

    @sync_to_async
    def save_async(self, room):
        self._save_room(room)

        
    def delete(self, room):
        orm_room = self.get_room_base(room.uuid)
        if orm_room:
            orm_room.delete()


    def get_all_by_user(user):
        return [RoomMapper.to_domain(room) for room in user.rooms.all()]
