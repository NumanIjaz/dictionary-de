import enum
from app.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum, Boolean
from sqlalchemy.sql import func

class PartOfSpeechEnum(enum.Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PRONOUN = "pronoun"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    ARTICLE = "article"
    NUMERAL = "numeral"
    OTHER = "other"

class GenderEnum(enum.Enum):
    MASCULINE = "masculine"
    FEMININE = "feminine"
    NEUTRAL = "neutral"
    OTHER = "other"

class AuxiliaryVerbEnum(enum.Enum):
    HABEN = "haben"
    SEIN = "sein"

class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)
    lemma = Column(String(255), index=True, nullable=False)
    part_of_speech = Column("part_of_speech", Enum(PartOfSpeechEnum), nullable=False)
    gender = Column(Enum(GenderEnum), nullable=True)

    plural_form = Column(String(255), nullable=True)
    separable = Column(Boolean, nullable=True)
    reflexive = Column(Boolean, nullable=True)
    auxiliary_verb = Column(Enum(AuxiliaryVerbEnum), nullable=True)

    comparative = Column(String(255), nullable=True)
    superlative = Column(String(255), nullable=True)

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
