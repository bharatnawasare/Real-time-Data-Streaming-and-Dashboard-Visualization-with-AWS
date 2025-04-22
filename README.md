# Contact-service-notes
# Contact Notes Backend

This is a simple backend service built using FastAPI for managing contacts and their associated notes. It features JWT-based authentication, RESTful API endpoints, and support for SQLite out of the box.

## 🚀 Features
- JWT Authentication
- CRUD operations for Contacts and Notes
- REST API with auto-generated documentation
- SQLite database with SQLAlchemy ORM
- Modular and easy-to-extend codebase

## 🛠️ Technologies Used
- Python 3.9+
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Python-Jose (for JWT)

## 📦 Installation
1. Open bash or Windows Powershell or Terminal or cmd

2. Clone the repository:
   git clone https://github.com/yourusername/contact-notes-backend.git
   cd contact-notes-backend
   ```
2. Set up a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Running the Application
1. Run the application with Uvicorn:
   ```bash
   uvicorn main:app --reload
   ```
2. Visit `http://127.0.0.1:8000/docs` to access the auto-generated Swagger UI for testing the APIs.

## 📌 API Endpoints
### Contacts
- `POST /contacts/` - Create a new contact
- `GET /contacts/` - List all contacts

### Notes
- `POST /notes/` - Create a new note
- `GET /notes/` - List all notes

## 🧪 Running Tests
(Testing setup will be added in the future)

## 📋 To Improve or Add
- Full JWT-based login and registration
- Unit and integration tests using pytest
- Pagination and filtering for listing APIs
- Rate limiting and retry handling
- Asynchronous note indexing using Celery + Redis

## 📨 Submission
1. Push the code to a public GitHub repository

---

> Practical, clear, and extensible backend design for managing contact notes.

