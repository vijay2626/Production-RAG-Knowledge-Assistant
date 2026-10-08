from contextlib import asynccontextmanager
from fastapi import FastAPI,Response
from prometheus_client import Counter,generate_latest,CONTENT_TYPE_LATEST
from app.core.database import Base,engine
from app.api.v1 import health,auth,documents,chat
from app.models import models
requests=Counter("rag_api_requests_total","Total RAG API requests")
@asynccontextmanager
async def lifespan(app): Base.metadata.create_all(bind=engine); yield
app=FastAPI(title="Production RAG Knowledge Assistant",version="1.0.0",lifespan=lifespan)
@app.middleware("http")
async def count(request,call_next): response=await call_next(request); requests.inc(); return response
app.include_router(health.router,prefix="/api/v1"); app.include_router(auth.router,prefix="/api/v1"); app.include_router(documents.router,prefix="/api/v1"); app.include_router(chat.router,prefix="/api/v1")
@app.get("/metrics",include_in_schema=False)
def metrics(): return Response(generate_latest(),media_type=CONTENT_TYPE_LATEST)
