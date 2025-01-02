import uuid
from dataclasses import dataclass, field
from typing import List
from datetime import datetime


@dataclass
class OrderItem:
    product_id: uuid.UUID
    price: float
    quantity: int

    def get_cost(self) -> float:
        return self.price * self.quantity


@dataclass
class Order:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    user_id: uuid.UUID = None
    full_name: str = ""
    email: str = ""
    address: str = ""
    address2: str = ""
    city: str = ""
    zip_code: str = ""
    country: str = ""
    phone: str = ""
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    is_paid: bool = False
    status: str = "Pending"
    items: List[OrderItem] = field(default_factory=list)

    STATUS = {
        'Pending': 'Pending',
        'Shipped': 'Shipped',
        'Delivered': 'Delivered',
        'Cancelled': 'Cancelled',
    }
    
    def get_total_cost(self) -> float:
        return sum(item.get_cost() for item in self.items)
