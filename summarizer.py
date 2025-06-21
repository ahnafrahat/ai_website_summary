import requests
from typing import Dict, Any, Optional
from config import Config
from website import Website

# Import IPython display functionality
try:
    from IPython.display import Markdown, display
    IPYTHON_AVAILABLE = True
except ImportError:
    IPYTHON_AVAILABLE = False


class WebsiteSummarizer:
    
    def __init__(self, api_url: Optional[str] = None, model: Optional[str] = None, use_openai: Optional[bool] = None):

        self.use_openai = use_openai if use_openai is not None else Config.USE_OPENAI
        
        if self.use_openai:
            # OpenAI configuration
            self.api_url = api_url or f"{Config.OPENAI_API_BASE}/chat/completions"
            self.model = model or Config.OPENAI_MODEL
            self.headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {Config.OPENAI_API_KEY}"
            }
            if not Config.OPENAI_API_KEY:
                raise ValueError("OPENAI_API_KEY is required when using OpenAI API")
        else:
            # Ollama configuration
            self.api_url = api_url or Config.OLLAMA_API_URL
            self.model = model or Config.OLLAMA_MODEL
            self.headers = {"Content-Type": "application/json"}
    
    def _create_messages(self, website: Website) -> list:

        summary_data = website.get_summary_data()
        user_prompt = Config.USER_PROMPT_TEMPLATE.format(
            title=summary_data["title"],
            content=summary_data["content"]
        )
        
        return [
            {"role": "system", "content": Config.SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    
    def _make_api_request(self, messages: list) -> Dict[str, Any]:

        if self.use_openai:
            # OpenAI API request
            payload = {
                "model": self.model,
                "messages": messages,
                "temperature": 0.7,
                "max_tokens": 1000
            }
        else:
            # Ollama API request
            payload = {
                "model": self.model,
                "messages": messages,
                "stream": False
            }
        
        try:
            response = requests.post(
                self.api_url, 
                json=payload, 
                headers=self.headers, 
                timeout=60
            )
            response.raise_for_status()
            
            result = response.json()
            
            if self.use_openai:
                # OpenAI response format
                if 'choices' not in result or not result['choices']:
                    raise ValueError("Invalid OpenAI API response format")
                return {'message': {'content': result['choices'][0]['message']['content']}}
            else:
                # Ollama response format
                if 'message' not in result or 'content' not in result['message']:
                    raise ValueError("Invalid Ollama API response format")
                return result
            
        except requests.RequestException as e:
            raise requests.RequestException(f"API request failed: {str(e)}")
        except ValueError as e:
            raise ValueError(f"Invalid API response: {str(e)}")
    
    def summarize(self, url: str) -> str:

        try:
            # Create website object
            website = Website(url)
            
            # Create messages for API
            messages = self._create_messages(website)
            
            # Make API request
            response = self._make_api_request(messages)
            
            # Return the summary
            return response['message']['content']
            
        except Exception as e:
            raise type(e)(f"Failed to summarize {url}: {str(e)}")
    
    def summarize_website_object(self, website: Website) -> str:
 
        messages = self._create_messages(website)
        response = self._make_api_request(messages)
        return response['message']['content']
    
    def display_summary(self, url: str) -> None:

        if not IPYTHON_AVAILABLE:
            raise ImportError("IPython is required for display_summary. Install with: pip install ipython")
        
        summary = self.summarize(url)
        display(Markdown(summary)) 