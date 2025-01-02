from client.infrastructure.orm.models import Address as OrmAddress
from client.infrastructure.orm.mappers import AddressMapper
from client.domain.entities import Address as DomainAddress


class AddressRepository:
    @staticmethod
    def save_address(address_entity: DomainAddress):
        address = AddressMapper.to_orm(address_entity)
        address.save()
        return AddressMapper.to_domain(address)

    @staticmethod
    def delete_address(address_entity: DomainAddress):
        address = OrmAddress.objects.get(id=address_entity.id)
        address.delete()
        return AddressMapper.to_domain(address)

    @staticmethod
    def get_addresses_by_user(user) -> list[DomainAddress]:
        orm_addresses = OrmAddress.objects.filter(user=user)
        return [AddressMapper.to_domain(address) for address in orm_addresses]

    @staticmethod
    def get_address_by_id_and_user(address_id, user) -> DomainAddress | None:
        try:
            address = OrmAddress.objects.get(id=address_id, user=user)
            return AddressMapper.to_domain(address)
        except OrmAddress.DoesNotExist:
            return None

    @staticmethod
    def get_address_instance(address_id, user) -> OrmAddress | None:
        try:
            return OrmAddress.objects.get(id=address_id, user=user)
        except OrmAddress.DoesNotExist:
            return None
