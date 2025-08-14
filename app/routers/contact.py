from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models import ContactMessage
from ..schemas import ContactCreate, ContactOut
from ..config import settings

router = APIRouter(prefix="/api/contact", tags=["contact"])

@router.post("/", response_model=ContactOut)
def create_message(payload: ContactCreate, db: Session = Depends(get_db)):
    msg = ContactMessage(
        name=payload.name,
        email=payload.email,
        subject=payload.subject,
        message=payload.message,
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg

@router.get("/", response_model=List[ContactOut])
def list_messages(
    db: Session = Depends(get_db),
    x_admin_token: str | None = Header(default=None, alias="X-Admin-Token"),
):
    if not x_admin_token or x_admin_token != settings.ADMIN_TOKEN:
        raise HTTPException(status_code=403, detail="Forbidden: invalid admin token")
    items = db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()
    return items
