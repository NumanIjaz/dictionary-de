import enum

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

class InflectionCategoryEnum(enum.Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    PRONOUN = "pronoun"
    OTHER = "other"

class InflectionCaseEnum(enum.Enum):
    NOMINATIVE = "nominative"
    ACCUSATIVE = "accusative"
    DATIVE = "dative"
    GENITIVE = "genitive"
