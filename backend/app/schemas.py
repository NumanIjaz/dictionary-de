import uuid
from pydantic import BaseModel

from app.enums import (
    GenderEnum,
    PartOfSpeechEnum,
    InflectionCategoryEnum,
    InflectionCaseEnum,
    AuxiliaryVerbEnum,
)


class Inflection(BaseModel):
    id: uuid.UUID | None = None
    category: InflectionCategoryEnum
    inflection_case: InflectionCaseEnum | None = None

    class Config:
        from_attributes = True


class Word(BaseModel):
    id: uuid.UUID | None = None
    lemma: str
    part_of_speech: PartOfSpeechEnum
    gender: GenderEnum | None = None
    plural_form: str | None = None
    separable: bool | None = None
    reflexive: bool | None = None
    auxiliary_verb: AuxiliaryVerbEnum | None = None
    comparative: str | None = None
    superlative: str | None = None

    inflections: list[Inflection] | None = None

    class Config:
        from_attributes = True
