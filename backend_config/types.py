from enum import auto, StrEnum


class Environment(StrEnum):
    DEVELOPMENT = auto()
    STAGING = auto()
    PRODUCTION = auto()
