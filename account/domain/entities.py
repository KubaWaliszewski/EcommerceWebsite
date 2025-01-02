import uuid
from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class DomainUser:
    email: str  
    first_name: str  
    last_name: str  
    id: uuid.UUID = field(default_factory=uuid.uuid4)  
    role: str = "client"  
    is_active: bool = True  
    is_staff: bool = False  
    date_joined: datetime = field(default_factory=datetime.utcnow)  
    last_login: Optional[datetime] = None  

    
    AGENT = 'agent'
    MANAGER = 'manager'
    CLIENT = 'client'

    ROLE_CHOICES = {AGENT, MANAGER, CLIENT}

    def __post_init__(self):
        if self.role not in self.ROLE_CHOICES:
            raise ValueError(f"Invalid role: {self.role}")
        if not self.email:
            raise ValueError("Email cannot be empty")

    def full_name(self) -> str:
        """Returns the full name of the user."""
        return f"{self.first_name} {self.last_name}"

