
import requests
from bs4 import BeautifulSoup
from config import Config
from typing import Optional


class Website:
    
    def __init__(self, url: str):

        if not url or not url.strip():
            raise ValueError("URL cannot be empty or None")
            
        self.url = url.strip()
        self.title: Optional[str] = None
        self.text: Optional[str] = None
        self._fetch_content()
    
    def _fetch_content(self) -> None:

        try:
            response = requests.get(self.url, headers=Config.HEADERS, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            self._extract_title(soup)
            self._extract_text(soup)
            
        except requests.RequestException as e:
            raise requests.RequestException(f"Failed to fetch website {self.url}: {str(e)}")
    
    def _extract_title(self, soup: BeautifulSoup) -> None:
        title_tag = soup.find('title')
        self.title = title_tag.string.strip() if title_tag and title_tag.string else "No title found"
    
    def _extract_text(self, soup: BeautifulSoup) -> None:
        for element in soup.find_all(['script', 'style', 'img', 'input', 'nav', 'header', 'footer']):
            element.decompose()
        
        body = soup.find('body')
        if body:
            self.text = body.get_text(separator="\n", strip=True)
        else:
            self.text = soup.get_text(separator="\n", strip=True)
        
        if self.text:
            self.text = " ".join(self.text.split())
    
    def get_summary_data(self) -> dict:

        return {
            "title": self.title,
            "content": self.text
        }
    
    def __str__(self) -> str:
        return f"Website(url='{self.url}', title='{self.title}')"
    
    def __repr__(self) -> str:
        return f"Website(url='{self.url}', title='{self.title}', text_length={len(self.text) if self.text else 0})"
