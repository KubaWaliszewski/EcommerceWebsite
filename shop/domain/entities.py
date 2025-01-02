from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Review:
    id: int
    user_id: int
    rating: int
    comment: Optional[str]
    created_at: datetime


@dataclass
class Category:
    id: int
    name: str
    slug: str
    created_at: datetime


@dataclass
class Product:
    id: int
    name: str
    slug: str
    description: Optional[str]
    price: float
    discount: float
    stock: int
    is_available: bool
    category: Category
    created_at: datetime
    updated_at: datetime
    image: Optional[str] = None
    reviews: Optional[list[Review]] = None

    def get_discounted_price(self):
        return self.price - (self.price * self.discount / 100)
