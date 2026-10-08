from datetime import datetime
from sqlalchemy import DateTime,ForeignKey,Integer,String,Text,func
from sqlalchemy.orm import Mapped,mapped_column
from pgvector.sqlalchemy import Vector
from app.core.database import Base
class User(Base):
    __tablename__="users"
    id:Mapped[int]=mapped_column(primary_key=True); email:Mapped[str]=mapped_column(String(255),unique=True,index=True); full_name:Mapped[str]=mapped_column(String(255)); password_hash:Mapped[str]=mapped_column(String(255)); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now())
class Document(Base):
    __tablename__="documents"
    id:Mapped[int]=mapped_column(primary_key=True); owner_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True); title:Mapped[str]=mapped_column(String(255)); content:Mapped[str]=mapped_column(Text); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now())
class DocumentChunk(Base):
    __tablename__="document_chunks"
    id:Mapped[int]=mapped_column(primary_key=True); document_id:Mapped[int]=mapped_column(ForeignKey("documents.id",ondelete="CASCADE"),index=True); chunk_index:Mapped[int]=mapped_column(Integer); content:Mapped[str]=mapped_column(Text); embedding:Mapped[list[float]]=mapped_column(Vector(32)); metadata_json:Mapped[str]=mapped_column(String(2000),default="{}")
class ConversationMessage(Base):
    __tablename__="conversation_messages"
    id:Mapped[int]=mapped_column(primary_key=True); user_id:Mapped[int]=mapped_column(ForeignKey("users.id"),index=True); role:Mapped[str]=mapped_column(String(20)); content:Mapped[str]=mapped_column(Text); created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),server_default=func.now())
