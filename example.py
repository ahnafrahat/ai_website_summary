
from website import Website
from summarizer import WebsiteSummarizer


def example_basic_usage():
    """Example of basic usage with URL."""
    print("=== Basic Usage Example ===")
    
    summarizer = WebsiteSummarizer()
    url = "https://ahnaf.adverlify.com/"
    
    try:
        summary = summarizer.summarize(url)
        print(f"Summary of {url}:")
        print(summary)
        print()
    except Exception as e:
        print(f"Error: {e}")


def example_advanced_usage():
    """Example of advanced usage with custom configuration."""
    print("=== Advanced Usage Example ===")
    
    summarizer = WebsiteSummarizer(
        api_url="http://localhost:11434/api/chat",
        model="llama3.2"
    )
    
    website = Website("https://ahnaf.adverlify.com/")
    
    try:
        summary = summarizer.summarize_website_object(website)
        print(f"Summary of {website.url}:")
        print(f"Title: {website.title}")
        print(f"Content length: {len(website.text) if website.text else 0} characters")
        print("\nSummary:")
        print(summary)
        print()
    except Exception as e:
        print(f"Error: {e}")


def example_display_summary():
    """Example of using display_summary method (for Jupyter/IPython)."""
    print("=== Display Summary Example ===")
    
    summarizer = WebsiteSummarizer()
    url = "https://ahnaf.adverlify.com/"
    
    try:
        print("Note: This method is designed for Jupyter notebooks or IPython environments.")
        print("In a regular Python script, it will still work but may not display as nicely.")
        print()
        
        summary = summarizer.summarize(url)
        print("Summary (would be displayed as Markdown in Jupyter):")
        print(summary)
        print()
        
    except Exception as e:
        print(f"Error: {e}")


def example_error_handling():
    """Example demonstrating error handling."""
    print("=== Error Handling Example ===")
    
    summarizer = WebsiteSummarizer()
    invalid_url = "https://invalid-url-that-does-not-exist.com/"
    
    try:
        summary = summarizer.summarize(invalid_url)
        print(summary)
    except Exception as e:
        print(f"Expected error for invalid URL: {e}")
        print()


if __name__ == "__main__":
    example_basic_usage()
    example_advanced_usage()
    example_display_summary()
    example_error_handling() 