import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .web_view import BrowserWebView
from .tab_label import TabLabel

class BrowserTab(Gtk.Box):
    def __init__(self, url, on_close):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        
        # Create WebView
        self.webview = BrowserWebView()
        self.pack_start(self.webview, True, True, 0)
        
        # Create tab label
        self.tab_label = TabLabel(lambda _: on_close(self))
        
        # Connect signals for title and URI changes
        self.webview.connect('notify::title', self._on_title_changed)
        self.webview.connect('notify::uri', self._on_uri_changed)
        
        # Load initial URL
        self.webview.navigate(url)
    
    def get_label_widget(self):
        """Get the tab label widget"""
        return self.tab_label
    
    def _on_title_changed(self, web_view, param):
        """Update tab label when page title changes"""
        title = web_view.get_title()
        if title:
            self.tab_label.set_text(title)
    
    def _on_uri_changed(self, web_view, param):
        """Update tab label when URI changes if no title is available"""
        if not web_view.get_title():
            uri = web_view.get_uri() or "New Tab"
            self.tab_label.set_text(uri)