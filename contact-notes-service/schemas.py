from pydantic import BaseModel
from typing import List

class NoteBase(BaseModel):
    body: str

class NoteCreate(NoteBase):
    pass

class Note(NoteBase):
    id: int
    contact_id: int
    class Config:
        orm_mode = True

class ContactBase(BaseModel):
    name: str
    email: str

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    id: int
    notes: List[Note] = []
    class Config:
        orm_mode = True
