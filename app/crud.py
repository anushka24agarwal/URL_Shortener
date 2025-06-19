import string, random
from sqlalchemy.orm import Session
from app import models

CHAR_SET = string.ascii_letters + string.digits


def generate_short_code(length: int = 6):
    return ''.join(random.choices(CHAR_SET, k=length))

def create_short_url(db: Session, original_url: str):
    short_code = generate_short_code()
    db_url = models.URL(short_code=short_code, original_url=original_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return {"short_code": db_url.short_code, "original_url": db_url.original_url}

def get_original_url(db: Session, short_code: str):
    url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    return url.original_url if url else None