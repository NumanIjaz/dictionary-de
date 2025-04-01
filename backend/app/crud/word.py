from sqlalchemy.orm import Session

from app import schemas
from app.models.word import Word


def get_word(db: Session, word_id: int) -> Word:
    return db.query(Word).filter(Word.id == word_id).first()

def get_words(db: Session, skip: int = 0, limit: int = 100) -> list[Word]:
    return db.query(Word).offset(skip).limit(limit).all()

def create_word(db: Session, input_word: schemas.Word) -> Word:
    db_word = Word(**input_word.model_dump())
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word
