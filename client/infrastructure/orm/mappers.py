from client.infrastructure.orm.models import Address as OrmAddress
from client.domain.entities import Address as DomainAddress
from account.infrastructure.orm.models import CustomUser

class AddressMapper:
    @staticmethod
    def to_domain(address: OrmAddress) -> DomainAddress:
        return DomainAddress(
            id=address.id,
            user=address.user, 
            first_name=address.first_name,
            last_name=address.last_name,
            address=address.address,
            address2=address.address2,
            city=address.city,
            zip_code=address.zip_code,
            country=address.country,
            phone=address.phone,
            default=address.default,
        )

    @staticmethod
    def to_orm(address_entity: DomainAddress) -> OrmAddress:
        user = CustomUser.objects.get(id=address_entity.user.id)
        address = OrmAddress(
            id=address_entity.id,
            user=user, 
            first_name=address_entity.first_name,
            last_name=address_entity.last_name,
            address=address_entity.address,
            address2=address_entity.address2,
            city=address_entity.city,
            zip_code=address_entity.zip_code,
            country=address_entity.country,
            phone=address_entity.phone,
            default=address_entity.default,
        )
        return address
    