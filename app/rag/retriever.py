from sqlalchemy import select
from sqlalchemy.orm import Session
from app.models.models import DocumentChunk
from app.ai.embeddings import EmbeddingService
class Retriever:
    def __init__(self,db:Session): self.db=db; self.emb=EmbeddingService()
    def search(self,q,top_k):
        v=self.emb.embed(q); distance=DocumentChunk.embedding.cosine_distance(v)
        return self.db.execute(select(DocumentChunk,distance.label("distance")).order_by(distance).limit(top_k)).all()
