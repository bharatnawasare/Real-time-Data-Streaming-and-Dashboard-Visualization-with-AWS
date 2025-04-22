from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Note
from schemas import NoteCreate, Note

router = APIRouter(prefix="/notes", tags=["notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=Note)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(body=note.body, contact_id=1)  # example contact_id
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

@router.get("/", response_model=list[Note])
def read_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()
