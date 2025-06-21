
import sys
from summarizer import WebsiteSummarizer


def main():
    url = "https://ahnaf.adverlify.com/"
    
    try:
        summarizer = WebsiteSummarizer()
        print(f"Summarizing: {url}")
        summary = summarizer.summarize(url)
        
        print("\n" + "="*50)
        print("SUMMARY")
        print("="*50)
        print(summary)
        print("="*50)
        
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
