from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    email_password: str
    email_user: str
    email_receiver: str

    class Config:
        env_file = '.env'

settings = Settings()