from app.core.config import get_settings
class LLMProvider:
    def generate(self,question,context):
        if get_settings().ai_provider=="mock": return "Grounded mock answer based on retrieved context: "+context[:700]
        return "Configure your selected LLM adapter in app/ai/providers.py."
