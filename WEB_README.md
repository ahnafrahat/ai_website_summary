# AI Website Summarizer - Web Application

A beautiful, modern web interface for the AI-powered website summarizer. This application provides an intuitive way to summarize any website using advanced AI technology.

## Features

- 🎨 **Modern UI/UX**: Beautiful, responsive design with dark theme
- ⚡ **Real-time Processing**: Live feedback during summarization
- 📱 **Mobile Responsive**: Works perfectly on all devices
- 🎯 **Smart Validation**: URL validation and error handling
- 📋 **Copy to Clipboard**: Easy summary copying functionality
- 🔄 **Reset & Retry**: Quick form reset and new summary generation

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Web Application

```bash
python app.py
```

### 3. Open Your Browser

Navigate to `http://localhost:5000` to access the application.

## Usage

1. **Enter URL**: Type or paste the website URL you want to summarize
2. **Click Summarize**: Press the "Summarize" button or hit Enter
3. **Wait for Processing**: The AI will analyze the website content
4. **View Results**: Read the generated summary in a beautiful format
5. **Copy or Reset**: Copy the summary or start a new one

## Project Structure

```
llm_website_summary/
├── app.py                 # Flask web application
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Beautiful CSS styling
│   └── js/
│       └── script.js     # Frontend JavaScript
├── summarizer.py         # Core summarization logic
├── website.py           # Website content extraction
├── config.py            # Configuration settings
└── requirements.txt     # Python dependencies
```

## API Endpoints

### POST /summarize

Summarizes a website given its URL.

**Request Body:**
```json
{
    "url": "https://example.com"
}
```

**Response:**
```json
{
    "success": true,
    "summary": "Generated summary content...",
    "url": "https://example.com"
}
```

## Configuration

Make sure your Ollama API is running and accessible. The application uses the configuration from `config.py`.

## Troubleshooting

### Common Issues

1. **"Failed to fetch website"**: Check if the URL is accessible and valid
2. **"API request failed"**: Ensure Ollama is running and accessible
3. **"Invalid URL"**: Make sure to include the protocol (http:// or https://)

### Development

For development, the Flask app runs in debug mode. To run in production:

```bash
export FLASK_ENV=production
python app.py
```

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge

## Contributing

Feel free to contribute to improve the UI/UX or add new features!

## License

This project is open source and available under the MIT License. 