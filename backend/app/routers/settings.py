import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import SiteSettings
from ..schemas import SiteSettingsOut

router = APIRouter(prefix="/settings", tags=["Settings"])


@router.get("", response_model=SiteSettingsOut)
def get_settings(db: Session = Depends(get_db)):
    settings = db.query(SiteSettings).first()
    if not settings:
        settings = SiteSettings(
            name="",
            title="",
            bio="",
            socials=json.dumps({}),
            meta_defaults=json.dumps({}),
        )
        db.add(settings)
        db.commit()
        db.refresh(settings)
    return SiteSettingsOut(
        id=settings.id,
        name=settings.name,
        title=settings.title,
        bio=settings.bio,
        socials=json.loads(settings.socials or "{}"),
        meta_defaults=json.loads(settings.meta_defaults or "{}"),
    )
