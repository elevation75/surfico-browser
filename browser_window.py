import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from components.browser_tab import BrowserTab
from components.window_controls import WindowControls
from toolbar import Toolbar

class BrowserWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Surfico Browser")
        self.set_default_size(1024, 768)

        # Create main vertical box
        self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.vbox)

        # Create header box
        header_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.vbox.pack_start(header_box, False, False, 0)

        # Create toolbar
        self.toolbar = Toolbar()
        self.toolbar.connect_signals(self)
        header_box.pack_start(self.toolbar, True, True, 0)

        # Add window controls
        self.window_controls = WindowControls(self)
        header_box.pack_end(self.window_controls, False, False, 5)

        # Create notebook for tabs
        self.notebook = Gtk.Notebook()
        self.notebook.set_scrollable(True)
        self.vbox.pack_start(self.notebook, True, True, 0)

        # Create first tab
        self.create_new_tab()

    def create_new_tab(self, url="https://www.arcolinux.info"):
        """Create a new browser tab"""
        tab = BrowserTab(url, self.on_tab_close_clicked)
        tab.webview.connect("load-changed", self.update_toolbar)
        
        page_num = self.notebook.append_page(tab, tab.get_label_widget())
        self.notebook.set_current_page(page_num)
        self.notebook.show_all()
        
        return tab

    def get_current_tab(self):
        """Get the currently active tab"""
        page_num = self.notebook.get_current_page()
        return self.notebook.get_nth_page(page_num)

    def on_tab_close_clicked(self, tab):
        """Handle tab close button click"""
        page_num = self.notebook.page_num(tab)
        
        if self.notebook.get_n_pages() == 1:
            # If this is the last tab, create a new empty tab before closing
            self.create_new_tab()
            
        self.notebook.remove_page(page_num)

    def update_toolbar(self, web_view, load_event):
        """Update toolbar buttons and URL entry"""
        current_tab = self.get_current_tab()
        if current_tab:
            self.toolbar.update_navigation_buttons(current_tab.webview)
            self.toolbar.update_url_entry(current_tab.webview)