from fastapi import APIRouter,Depends
from fastapi.security import HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import bearer,current_user
from app.core.config import get_settings
from app.models.models import ConversationMessage
from app.rag.pipeline import RAGPipeline
from pydantic import BaseModel,Field
router=APIRouter(prefix="/chat",tags=["rag"])
class Chat(BaseModel): question:str=Field(min_length=2); top_k:int=Field(default=5,ge=1,le=20)
@router.post("")
def chat(p:Chat,c:HTTPAuthorizationCredentials=Depends(bearer),db:Session=Depends(get_db)):
    u=current_user(c); a,cites=RAGPipeline(db).answer(p.question,p.top_k or get_settings().rag_top_k)
    db.add(ConversationMessage(user_id=int(u["sub"]),role="user",content=p.question)); db.add(ConversationMessage(user_id=int(u["sub"]),role="assistant",content=a)); db.commit()
    return {"answer":a,"citations":cites}
