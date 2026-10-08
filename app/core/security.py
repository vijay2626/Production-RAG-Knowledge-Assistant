from datetime import datetime,timedelta,timezone
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer
from jose import JWTError,jwt
from passlib.context import CryptContext
from app.core.config import get_settings
pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")
bearer=HTTPBearer()
def hash_password(p): return pwd.hash(p)
def verify_password(p,h): return pwd.verify(p,h)
def create_token(uid,email):
    s=get_settings(); exp=datetime.now(timezone.utc)+timedelta(minutes=s.jwt_expire_minutes)
    return jwt.encode({"sub":str(uid),"email":email,"exp":exp},s.jwt_secret,algorithm=s.jwt_algorithm)
def current_user(c:HTTPAuthorizationCredentials):
    s=get_settings()
    try: return jwt.decode(c.credentials,s.jwt_secret,algorithms=[s.jwt_algorithm])
    except JWTError as e: raise HTTPException(401,"Invalid or expired token") from e
