from app.rag.chunker import TextChunker
from app.ai.embeddings import EmbeddingService
def test_chunking(): assert len(TextChunker(5,1).split("one two three four five six seven"))>=2
def test_embedding_size(): assert len(EmbeddingService().embed("hello"))==32
