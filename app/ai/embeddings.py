class EmbeddingService:
    def embed(self,text:str)->list[float]:
        v=[float((ord(c)%31)/31) for c in text[:32]]
        return v+[0.0]*(32-len(v))
