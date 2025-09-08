from pydantic import BaseModel
from typing import Optional

# ------------------ USERS ------------------
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    role: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    is_verified: bool
    verification_status: str

    class Config:
        orm_mode = True

# ------------------ ARTWORKS ------------------
class ArtworkBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float = 0.0
    image_url: Optional[str] = None

class ArtworkCreate(ArtworkBase):
    pass

class ArtworkResponse(ArtworkBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# ------------------ ORDERS ------------------
class OrderResponse(BaseModel):
    id: int
    customer_id: int
    artwork_id: int
    quantity: int
    status: str

    class Config:
        orm_mode = True

# ------------------ NOTIFICATIONS ------------------
class NotificationResponse(BaseModel):
    id: int
    user_id: int
    message: str

    class Config:
        orm_mode = True

# ------------------ REQUESTS ------------------
class RequestResponse(BaseModel):
    id: int
    title: str
    description: str
    requester_id: int

    class Config:
        orm_mode = True
