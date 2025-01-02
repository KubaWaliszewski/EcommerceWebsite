from dataclasses import dataclass
from typing import List


@dataclass
class CartItem:
    id: int
    product_price: float
    quantity: int
    cart_id: int
    product_id: int

    def get_total_price(self) -> float:
        return self.product_price * self.quantity


@dataclass
class Cart:
    id: int
    created_at: str
    items: List[CartItem]

    def get_total_price(self) -> float:
        return sum(item.get_total_price() for item in self.items)

    def get_total_quantity(self) -> int:
        return sum(item.quantity for item in self.items)