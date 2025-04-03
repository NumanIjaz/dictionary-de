from sqlalchemy.orm import Session

from app import schemas
from app.models.word import Word, WordInflection


def get_word(db: Session, word_id: int) -> Word:
    return db.query(Word).filter(Word.id == word_id).first()

def get_words(db: Session, skip: int = 0, limit: int = 100) -> list[Word]:
    return db.query(Word).offset(skip).limit(limit).all()

def create_word(db: Session, input_word: schemas.Word) -> Word:
    input_word_dict = input_word.model_dump()
    del input_word_dict["id"]
    del input_word_dict["inflections"]
    # del input_word_dict["created_at"]
    # del input_word_dict["updated_at"]
    db_word = Word(**input_word_dict)
    db_word.inflections = [
        WordInflection(**inflection.model_dump()) for inflection in input_word.inflections
    ]
    db.add(db_word)
    db.commit()
    db.refresh(db_word)
    return db_word
