from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, Text
from sqlalchemy.orm import relationship
from backend.app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="seller")  # seller or customer
    is_verified = Column(Boolean, default=False)
    verification_status = Column(String, default="pending")  # pending/verified/rejected
    proof_url = Column(String, nullable=True)

    artworks = relationship("Artwork", back_populates="owner")

class Artwork(Base):
    __tablename__ = "artworks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    price = Column(Float)
    image_url = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="artworks")

class ArtRequest(Base):
    __tablename__ = "art_requests"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    requester_id = Column(Integer, ForeignKey("users.id"))

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    message = Column(Text)

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("users.id"))
    artwork_id = Column(Integer, ForeignKey("artworks.id"))
    quantity = Column(Integer, default=1)
    status = Column(String, default="pending")
