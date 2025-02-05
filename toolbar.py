import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class Toolbar(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

        # Back button
        self.back_button = Gtk.Button.new_from_icon_name("go-previous", Gtk.IconSize.BUTTON)
        self.pack_start(self.back_button, False, False, 0)

        # Forward button
        self.forward_button = Gtk.Button.new_from_icon_name("go-next", Gtk.IconSize.BUTTON)
        self.pack_start(self.forward_button, False, False, 0)

        # Refresh button
        self.refresh_button = Gtk.Button.new_from_icon_name("view-refresh", Gtk.IconSize.BUTTON)
        self.pack_start(self.refresh_button, False, False, 0)

        # New tab button
        self.new_tab_button = Gtk.Button.new_from_icon_name("tab-new", Gtk.IconSize.BUTTON)
        self.pack_start(self.new_tab_button, False, False, 0)

        # URL entry
        self.url_entry = Gtk.Entry()
        self.pack_start(self.url_entry, True, True, 0)

    def connect_signals(self, window):
        """Connect toolbar signals to window methods"""
        self.back_button.connect("clicked", lambda w: window.get_current_tab().webview.go_back())
        self.forward_button.connect("clicked", lambda w: window.get_current_tab().webview.go_forward())
        self.refresh_button.connect("clicked", lambda w: window.get_current_tab().webview.reload())
        self.new_tab_button.connect("clicked", lambda w: window.create_new_tab())
        self.url_entry.connect("activate", self.on_url_activated, window)

    def on_url_activated(self, entry, window):
        """Handle URL entry activation"""
        url = entry.get_text()
        if not url.startswith(("http://", "https://")):
            url = "http://" + url
        window.get_current_tab().webview.load_uri(url)

    def update_navigation_buttons(self, webview):
        """Update navigation button states"""
        self.back_button.set_sensitive(webview.can_go_back())
        self.forward_button.set_sensitive(webview.can_go_forward())

    def update_url_entry(self, webview):
        """Update URL entry text"""
        uri = webview.get_uri()
        if uri:
            self.url_entry.set_text(uri)