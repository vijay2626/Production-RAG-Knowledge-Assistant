class TextChunker:
    def __init__(self,size=500,overlap=50): self.size=size; self.overlap=overlap
    def split(self,text):
        words=text.split(); step=max(1,self.size-self.overlap); out=[]
        for i in range(0,len(words),step):
            c=" ".join(words[i:i+self.size])
            if c: out.append(c)
            if i+self.size>=len(words): break
        return out
