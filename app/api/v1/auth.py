from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import hash_password,verify_password,create_token
from app.models.models import User
from pydantic import BaseModel,EmailStr,Field
router=APIRouter(prefix="/auth",tags=["auth"])
class Register(BaseModel): email:EmailStr; password:str=Field(min_length=8); full_name:str=Field(min_length=2)
class Login(BaseModel): email:EmailStr; password:str
@router.post("/register",status_code=201)
def register(p:Register,db:Session=Depends(get_db)):
    if db.scalar(select(User).where(User.email==p.email)): raise HTTPException(409,"Email already registered")
    u=User(email=p.email,full_name=p.full_name,password_hash=hash_password(p.password)); db.add(u); db.commit(); db.refresh(u)
    return {"id":u.id,"email":u.email,"full_name":u.full_name}
@router.post("/login")
def login(p:Login,db:Session=Depends(get_db)):
    u=db.scalar(select(User).where(User.email==p.email))
    if not u or not verify_password(p.password,u.password_hash): raise HTTPException(401,"Invalid email or password")
    return {"access_token":create_token(u.id,u.email),"token_type":"bearer"}
