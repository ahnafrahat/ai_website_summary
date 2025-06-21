
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    
    # Ollama API settings
    OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/chat")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
    
    # OpenAI API settings
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_API_BASE = os.getenv("OPENAI_API_BASE", "https://api.openai.com/v1")
    
    # Model selection
    USE_OPENAI = os.getenv("USE_OPENAI", "false").lower() == "true"
    
    # HTTP settings
    HEADERS = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
    }
    
    # Prompt templates
    SYSTEM_PROMPT = """You are an assistant that analyzes the contents of a website 
and provides a short summary, ignoring text that might be navigation related. 
Respond in markdown."""
    
    USER_PROMPT_TEMPLATE = """You are looking at a website titled {title}
The contents of this website is as follows; please provide a short summary of this website in markdown. 
If it includes news or announcements, then summarize these too.

{content}""" 