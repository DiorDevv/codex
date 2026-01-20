import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .auth import get_password_hash
from .db import SessionLocal, engine
from .models import Base, User
from .routers import admin, auth, blog, contact, projects, settings

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ProFolio API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(blog.router)
app.include_router(settings.router)
app.include_router(contact.router)
app.include_router(admin.router)


@app.on_event("startup")
def ensure_admin_user():
    db: Session = SessionLocal()
    try:
        admin_email = os.getenv("ADMIN_EMAIL", "admin@example.com")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
        admin = db.query(User).filter(User.email == admin_email).first()
        if not admin:
            admin = User(
                email=admin_email,
                hashed_password=get_password_hash(admin_password),
                is_admin=True,
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()
