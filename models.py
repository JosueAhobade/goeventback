from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base

# Table d'association pour likes/participations
event_user_table = Table(
    "event_user",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("event_id", ForeignKey("events.id"), primary_key=True)
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    # relation vers ses événements créés
    events = relationship("Event", back_populates="owner")

    # événements likés/participés
    liked_events = relationship("Event", secondary=event_user_table, back_populates="liked_by")


class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)

    events = relationship("Event", back_populates="category")


class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)

    # relations
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="events")

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="events")

    liked_by = relationship("User", secondary=event_user_table, back_populates="liked_events")
