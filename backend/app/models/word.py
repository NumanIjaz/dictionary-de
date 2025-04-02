import enum
import uuid
from app.database import Base
from sqlalchemy import Column, String, DateTime, Enum, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID

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

class InflectionCategory(enum.Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    PRONOUN = "pronoun"
    OTHER = "other"

class InflectionCase(enum.Enum):
    NOMINATIVE = "nominative"
    ACCUSATIVE = "accusative"
    DATIVE = "dative"
    GENITIVE = "genitive"

class Word(Base):
    __tablename__ = "words"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    lemma = Column(String(255), index=True, nullable=False)
    part_of_speech = Column("part_of_speech", Enum(PartOfSpeechEnum), nullable=False)
    gender = Column(Enum(GenderEnum), nullable=True)

    plural_form = Column(String(255), nullable=True)
    separable = Column(Boolean, nullable=True)
    reflexive = Column(Boolean, nullable=True)
    auxiliary_verb = Column(Enum(AuxiliaryVerbEnum), nullable=True)

    comparative = Column(String(255), nullable=True)
    superlative = Column(String(255), nullable=True)

    inclections: Mapped[list["WordInflection"]] = relationship(
        back_populates="word", cascade="all, delete"
    )

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

class WordInflection(Base):
    """
    Stores conjugations and declensions of words.
    """
    __tablename__ = "word_inflections"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    word_id: Mapped[UUID] = mapped_column(ForeignKey("words.id"))
    word: Mapped["Word"] = relationship(back_populates="inclections")

    category = Column(Enum(InflectionCategory), nullable=False)
    inflection_case = Column(Enum(InflectionCase), nullable=True)
