from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud, database
import logging
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/shorten", response_model=schemas.URLResponse)
def create_url(request: schemas.URLRequest, db: Session = Depends(database.get_db)):
    try:
        return crud.create_short_url(db, request.url)
    except Exception as e:
        logging.exception("Error occurred in /shorten")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/{short_code}", response_model=schemas.URLResponse)
def redirect(short_code: str, db: Session = Depends(database.get_db)):
    original_url = crud.get_original_url(db, short_code)
    if not original_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(url=original_url)
