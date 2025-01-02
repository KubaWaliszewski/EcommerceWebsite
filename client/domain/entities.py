from dataclasses import dataclass
from account.domain.entities import DomainUser


@dataclass
class Address:
    id: int
    user: DomainUser
    first_name: str
    last_name: str
    address: str
    address2: str
    city: str
    zip_code: int
    country: str
    phone: int
    default: bool
    