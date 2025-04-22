from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    notes = relationship("Note", back_populates="contact")

class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True, index=True)
    body = Column(String)
    contact_id = Column(Integer, ForeignKey("contacts.id"))
    contact = relationship("Contact", back_populates="notes")
