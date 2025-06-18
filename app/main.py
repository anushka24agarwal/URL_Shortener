from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

@app.post("/shorten")
def create_url(request: schemas.URLRequest, db: Session = Depends(database.get_db)):
    return crud.create_short_url(db, request.url)

@app.get("/{short_code}")
def redirect(short_code: str, db: Session = Depends(database.get_db)):
    original_url = crud.get_original_url(db, short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"original_url": original_url}
