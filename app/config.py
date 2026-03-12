from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Project Dan Maje API"
    app_env: str = "production"
    debug: bool = False
    secret_key: str = "change-me"
    jwt_secret: str = "change-me-too"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 1440
    database_url: str = "postgresql://postgres:postgres@localhost:5432/danmaje"
    frontend_origin: str = "https://your-vercel-app.vercel.app"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
