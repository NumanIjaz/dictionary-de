import uuid
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app import schemas
from app.database import get_db
from app.crud import word as word_crud

word_router = APIRouter(prefix="/words")

@word_router.get("/{word_id}", response_model=schemas.Word)
async def get_word(word_id: uuid.UUID, db: Session = Depends(get_db)) -> schemas.Word:
    word = word_crud.get_word(db, word_id)
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")
    return word


@word_router.get("/", response_model=list[schemas.Word])
async def get_words(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list[schemas.Word]:
    return word_crud.get_words(db, skip=skip, limit=limit)


@word_router.post("/", response_model=schemas.Word)
async def create_word(word_input: schemas.Word, db: Session = Depends(get_db)) -> schemas.Word:
    return word_crud.create_word(db, input_word=word_input)
