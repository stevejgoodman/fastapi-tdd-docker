import logging
from functools import lru_cache

from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")

class Settings:
    environment: str="dev"
    testing: bool=bool(0)

@lru_cache()
def get_settings()-> BaseSettings:
    log.info("loading config settings into environment")
    return Settings()






