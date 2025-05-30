from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "supersecretkey"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 1 day
    SMTP_SERVER: str = "smtp.example.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "user@example.com"
    SMTP_PASSWORD: str = "emailpassword"
    REDIS_URL: str = "redis://localhost:6379/0"
    DATABASE_URLOptional (STARTTLS on all ports)Credentials: str = "sqlite+aiosqlite:///./dlp.db"

settings = Settings()
