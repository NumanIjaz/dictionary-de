from pydantic import BaseModel

class Word(BaseModel):
    id: int | None = None
    word: str
    definition: str = ""

    class Config:
        from_attributes = True
