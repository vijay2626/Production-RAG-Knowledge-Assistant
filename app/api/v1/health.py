from fastapi import APIRouter
from sqlalchemy import text
from app.core.database import engine
router=APIRouter()
@router.get("/health")
def health(): return {"status":"ok","service":"rag-assistant"}
@router.get("/ready")
def ready():
    with engine.connect() as c: c.execute(text("SELECT 1"))
    return {"status":"ready"}
