
from flask import Flask, render_template, request, jsonify
from summarizer import WebsiteSummarizer
import traceback

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')

@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    """API endpoint to summarize a website."""
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        summarizer = WebsiteSummarizer()
        summary = summarizer.summarize(url)
        
        return jsonify({
            'success': True,
            'summary': summary,
            'url': url
        })
        
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000) 