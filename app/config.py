from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, field_validator
from typing import List, Union
import os


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""
    
    bot_token: str = Field(..., alias="BOT_TOKEN")
    admin_ids: List[int] = Field(default_factory=list, alias="ADMIN_IDS")
    db_path: str = Field(default="data/database.sqlite3", alias="DB_PATH")
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @field_validator("admin_ids", mode="before")
    @classmethod
    def parse_admin_ids(cls, v: Union[str, int, List[int]]) -> List[int]:
        """Parse ADMIN_IDS from comma-separated string or single int."""
        if isinstance(v, list):
            return v
        if isinstance(v, int):
            return [v]
        if isinstance(v, str):
            return [int(x.strip()) for x in v.split(",") if x.strip()]
        return []

    @property
    def database_url(self) -> str:
        """Get database path and ensure directory exists."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        return self.db_path


# Global instance
settings = Settings()

