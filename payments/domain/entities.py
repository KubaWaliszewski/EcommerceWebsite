import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Payment:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    order_id: uuid.UUID = None
    transaction_id: str = None
    amount: float = 0.0
    currency: str = "PLN"
    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)
    status: str = "Pending"
