def build_prompt(question,context):
    return f"Answer only from context. If insufficient, say so.\nCONTEXT:\n{context}\nQUESTION:\n{question}"
