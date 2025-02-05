import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2

class BrowserWebView(WebKit2.WebView):
    def __init__(self):
        super().__init__()
        
    def navigate(self, url):
        """Navigate to a URL, adding http:// if needed"""
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        self.load_uri(url)
        
    def can_navigate_back(self):
        """Check if we can navigate back"""
        return self.can_go_back()
        
    def can_navigate_forward(self):
        """Check if we can navigate forward"""
        return self.can_go_forward()
        
    def get_page_title(self):
        """Get the current page title or URL"""
        return self.get_title() or self.get_uri() or "New Tab"