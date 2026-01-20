from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import ContactMessage
from ..schemas import ContactCreate, ContactOut

router = APIRouter(prefix="/contact", tags=["Contact"])


@router.post("", response_model=ContactOut)
def submit_contact(payload: ContactCreate, db: Session = Depends(get_db)):
    message = ContactMessage(name=payload.name, email=payload.email, message=payload.message)
    db.add(message)
    db.commit()
    db.refresh(message)
    return message
