// DOM Elements
const summarizeForm = document.getElementById('summarizeForm');
const urlInput = document.getElementById('urlInput');
const submitBtn = document.getElementById('submitBtn');
const loadingState = document.getElementById('loadingState');
const resultsSection = document.getElementById('resultsSection');
const resultUrl = document.getElementById('resultUrl');
const summaryContent = document.getElementById('summaryContent');
const errorState = document.getElementById('errorState');
const errorMessage = document.getElementById('errorMessage');

// Form submission handler
summarizeForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const url = urlInput.value.trim();
    
    if (!url) {
        showError('Please enter a valid URL');
        return;
    }
    
    if (!isValidUrl(url)) {
        showError('Please enter a valid URL (e.g., https://example.com)');
        return;
    }
    
    await processSummary(url);
});

// URL validation
function isValidUrl(string) {
    try {
        new URL(string);
        return true;
    } catch (_) {
        return false;
    }
}

// Process summary request
async function processSummary(url) {
    try {
        // Show loading state
        showLoading(true);
        hideResults();
        hideError();
        
        // Disable form
        submitBtn.disabled = true;
        urlInput.disabled = true;
        
        // Make API request
        const response = await fetch('/summarize', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url: url })
        });
        
        const data = await response.json();
        
        if (!response.ok) {
            throw new Error(data.error || 'Failed to generate summary');
        }
        
        // Display results
        displayResults(url, data.summary);
        
    } catch (error) {
        console.error('Error:', error);
        showError(error.message || 'An unexpected error occurred');
    } finally {
        // Hide loading state
        showLoading(false);
        
        // Re-enable form
        submitBtn.disabled = false;
        urlInput.disabled = false;
    }
}

// Show/hide loading state
function showLoading(show) {
    if (show) {
        loadingState.classList.remove('hidden');
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Processing...';
    } else {
        loadingState.classList.add('hidden');
        submitBtn.innerHTML = '<span class="btn-text">Summarize</span><i class="fas fa-magic btn-icon"></i>';
    }
}

// Display results
function displayResults(url, summary) {
    resultUrl.textContent = url;
    summaryContent.innerHTML = formatSummary(summary);
    resultsSection.classList.remove('hidden');
    
    // Smooth scroll to results
    resultsSection.scrollIntoView({ 
        behavior: 'smooth',
        block: 'start'
    });
}

// Format summary content (convert markdown to HTML)
function formatSummary(summary) {
    let formatted = summary
        // Headers
        .replace(/^### (.*$)/gim, '<h3>$1</h3>')
        .replace(/^## (.*$)/gim, '<h2>$1</h2>')
        .replace(/^# (.*$)/gim, '<h1>$1</h1>')
        
        // Bold
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/__(.*?)__/g, '<strong>$1</strong>')
        
        // Italic
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/_(.*?)_/g, '<em>$1</em>')
        
        // Code blocks
        .replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>')
        .replace(/`([^`]+)`/g, '<code>$1</code>')
        
        // Lists
        .replace(/^\* (.*$)/gim, '<li>$1</li>')
        .replace(/^- (.*$)/gim, '<li>$1</li>')
        .replace(/^\d+\. (.*$)/gim, '<li>$1</li>')
        
        // Line breaks
        .replace(/\n\n/g, '</p><p>')
        .replace(/\n/g, '<br>');
    
    // Wrap in paragraphs if not already wrapped
    if (!formatted.startsWith('<h') && !formatted.startsWith('<p')) {
        formatted = '<p>' + formatted + '</p>';
    }
    
    // Fix list formatting
    formatted = formatted
        .replace(/<li>.*?<\/li>/g, function(match) {
            return '<ul>' + match + '</ul>';
        })
        .replace(/<\/ul>\s*<ul>/g, '');
    
    return formatted;
}

// Hide results
function hideResults() {
    resultsSection.classList.add('hidden');
}

// Show error
function showError(message) {
    errorMessage.textContent = message;
    errorState.classList.remove('hidden');
}

// Hide error
function hideError() {
    errorState.classList.add('hidden');
}

// Reset form
function resetForm() {
    urlInput.value = '';
    hideResults();
    hideError();
    urlInput.focus();
}

// Copy summary to clipboard
async function copySummary() {
    try {
        const summaryText = summaryContent.innerText;
        await navigator.clipboard.writeText(summaryText);
        
        // Show success feedback
        const originalText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fas fa-check"></i> Copied!';
        submitBtn.style.background = 'var(--success-green)';
        
        setTimeout(() => {
            submitBtn.innerHTML = originalText;
            submitBtn.style.background = '';
        }, 2000);
        
    } catch (error) {
        console.error('Failed to copy:', error);
        showError('Failed to copy summary to clipboard');
    }
}

// Close error modal when clicking outside
errorState.addEventListener('click', (e) => {
    if (e.target === errorState) {
        hideError();
    }
});

// Handle Enter key in URL input
urlInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        summarizeForm.dispatchEvent(new Event('submit'));
    }
});

// Add some nice animations and interactions
document.addEventListener('DOMContentLoaded', () => {
    // Animate hero section on load
    const heroContent = document.querySelector('.hero-content');
    heroContent.style.opacity = '0';
    heroContent.style.transform = 'translateY(30px)';
    
    setTimeout(() => {
        heroContent.style.transition = 'all 0.8s ease';
        heroContent.style.opacity = '1';
        heroContent.style.transform = 'translateY(0)';
    }, 100);
    
    // Add focus effects to input
    urlInput.addEventListener('focus', () => {
        urlInput.parentElement.style.transform = 'scale(1.02)';
    });
    
    urlInput.addEventListener('blur', () => {
        urlInput.parentElement.style.transform = 'scale(1)';
    });
    
    // Add hover effects to action buttons
    const actionBtns = document.querySelectorAll('.action-btn');
    actionBtns.forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            btn.style.transform = 'translateY(-2px)';
        });
        
        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translateY(0)';
        });
    });
});

// Add smooth scrolling for navigation links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Add loading animation for better UX
function addLoadingAnimation() {
    const dots = document.createElement('div');
    dots.className = 'loading-dots';
    dots.innerHTML = '<span></span><span></span><span></span>';
    
    const style = document.createElement('style');
    style.textContent = `
        .loading-dots {
            display: inline-flex;
            gap: 4px;
        }
        .loading-dots span {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--accent-purple);
            animation: loading-dots 1.4s infinite ease-in-out;
        }
        .loading-dots span:nth-child(1) { animation-delay: -0.32s; }
        .loading-dots span:nth-child(2) { animation-delay: -0.16s; }
        @keyframes loading-dots {
            0%, 80%, 100% { transform: scale(0); }
            40% { transform: scale(1); }
        }
    `;
    
    document.head.appendChild(style);
}

// Initialize loading animation
addLoadingAnimation(); 