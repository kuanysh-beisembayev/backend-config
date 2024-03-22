from pydantic_settings import BaseSettings

from backend_config.types import Environment


class CommonSettings(BaseSettings):
    debug: bool = False
    environment: Environment = Environment.DEVELOPMENT
