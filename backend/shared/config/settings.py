from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    app_name: str = "SkyBound Travels"

    environment: str = "Development"

    debug: bool = True

    database_url: str = "sqlite:///travel.db"

    log_level: str = "INFO"

    class Config:
        env_file = ".env"


settings = Settings()