from langchain.chat_models import init_chat_model
from langchain_ollama import ChatOllama

from app.core.config import settings

# GROQ_API_KEY = settings.GROQ_API_KEY


model_llama3_2_3b = ChatOllama(model="llama3.2:3b", temperature=0)

# model_groq_llama_3_1_8b_instant = init_chat_model("groq:llama-3.1-8b-instant", api_key=GROQ_API_KEY)
