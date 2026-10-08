from fastapi import APIRouter,Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import bearer,current_user
from app.models.models import Document,DocumentChunk
from app.rag.chunker import TextChunker
from app.ai.embeddings import EmbeddingService
from pydantic import BaseModel,Field
router=APIRouter(prefix="/documents",tags=["documents"])
class DocumentCreate(BaseModel): title:str=Field(min_length=1); content:str=Field(min_length=1)
@router.post("")
def create(p:DocumentCreate,c:HTTPAuthorizationCredentials=Depends(bearer),db:Session=Depends(get_db)):
    u=current_user(c); d=Document(owner_id=int(u["sub"]),title=p.title,content=p.content); db.add(d); db.commit(); db.refresh(d)
    chunks=TextChunker().split(p.content); emb=EmbeddingService()
    for i,t in enumerate(chunks): db.add(DocumentChunk(document_id=d.id,chunk_index=i,content=t,embedding=emb.embed(t)))
    db.commit(); return {"document_id":d.id,"chunks_created":len(chunks)}
@router.get("")
def list_docs(c:HTTPAuthorizationCredentials=Depends(bearer),db:Session=Depends(get_db)):
    u=current_user(c); return [{"id":d.id,"title":d.title} for d in db.scalars(select(Document).where(Document.owner_id==int(u["sub"]))).all()]
