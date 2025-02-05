import gi
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
from gi.repository import Gtk, WebKit2, Pango

class BrowserTab(Gtk.Box):
    def __init__(self, url):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.VERTICAL)
        
        # Create WebView
        self.webview = WebKit2.WebView()
        self.pack_start(self.webview, True, True, 0)
        
        # Store reference to tab label
        self.tab_label = None
        
        # Connect title changed signal
        self.webview.connect('notify::title', self.on_title_changed)
        self.webview.connect('notify::uri', self.on_title_changed)
        
        # Load initial URL
        self.webview.load_uri(url)
    
    def set_tab_label(self, label_box):
        """Store reference to tab label for later updates"""
        self.tab_label = label_box
    
    def on_title_changed(self, web_view, param):
        """Update tab label when page title changes"""
        if self.tab_label:
            title = web_view.get_title()
            if not title:
                title = web_view.get_uri() or "New Tab"
            label = self.tab_label.get_children()[0]  # Get the label widget
            label.set_text(title)
            label.set_ellipsize(Pango.EllipsizeMode.END)
            label.set_max_width_chars(25)