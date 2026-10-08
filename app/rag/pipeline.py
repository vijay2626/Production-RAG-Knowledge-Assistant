from app.ai.embeddings import EmbeddingService
from app.ai.providers import LLMProvider
from app.rag.retriever import Retriever
class RAGPipeline:
    def __init__(self,db): self.r=Retriever(db); self.llm=LLMProvider(); self.emb=EmbeddingService()
    def answer(self,q,top_k):
        rows=self.r.search(q,top_k); context="\n\n".join(x.content for x,d in rows)
        answer=self.llm.generate(q,context)
        citations=[{"chunk_id":x.id,"document_id":x.document_id,"score":round(1-float(d),4)} for x,d in rows]
        return answer,citations
