from fastapi import FastAPI
from database import Base, engine
from routes import contacts, notes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(contacts.router)
app.include_router(notes.router)
