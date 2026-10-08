from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    database_url:str="postgresql+psycopg://postgres:postgres@localhost:5432/rag_db"
    redis_url:str="redis://localhost:6379/0"
    jwt_secret:str="dev-secret"
    jwt_algorithm:str="HS256"
    jwt_expire_minutes:int=60
    ai_provider:str="mock"
    rag_top_k:int=5
    chunk_size:int=500
    chunk_overlap:int=50
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")
@lru_cache
def get_settings(): return Settings()
