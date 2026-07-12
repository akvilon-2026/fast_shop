from pydantic_settings import BaseSettings
from typing import List  # 👈 импортируем List


class Settings(BaseSettings):
    app_name: str = "FastAPI shop"  # исправил опечатку в FastAPI
    debug: bool = True              # исправил dedug → debug
    database_url: str = "sqlite:///./shop.db"
    cors_origins: List[str] = [     # 👈 правильный синтаксис
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ]
    static_dir: str = "static"
    images_dir: str="static/image"
    class Config:                   # 👈 ВНУТРИ класса Settings
        env_file = ".env"


settings = Settings()
