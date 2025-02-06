import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from bookmarks_storage import BookmarksStorage

class BookmarksButton(Gtk.Box):
    def __init__(self, window):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.window = window
        self.storage = BookmarksStorage()
        
        # Create bookmarks button
        self.bookmarks_button = Gtk.Button()
        self.bookmarks_button.set_relief(Gtk.ReliefStyle.NONE)
        bookmark_icon = Gtk.Image.new_from_icon_name("bookmark-new-symbolic", Gtk.IconSize.MENU)
        self.bookmarks_button.set_image(bookmark_icon)
        self.bookmarks_button.connect("clicked", self._on_bookmarks_clicked)
        
        # Pack bookmark button
        self.pack_start(self.bookmarks_button, False, False, 0)
    
    def _create_bookmark_row(self, bookmark):
        """Create a row for a bookmark with title and remove button"""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        
        # Create button with bookmark title
        button = Gtk.ModelButton(label=bookmark['title'])
        button.connect("clicked", self._on_bookmark_clicked, bookmark['url'])
        row.pack_start(button, True, True, 0)
        
        # Create remove button
        remove_btn = Gtk.Button()
        remove_btn.set_relief(Gtk.ReliefStyle.NONE)
        remove_icon = Gtk.Image.new_from_icon_name("window-close-symbolic", Gtk.IconSize.MENU)
        remove_btn.set_image(remove_icon)
        remove_btn.connect("clicked", self._on_remove_bookmark, bookmark['url'])
        row.pack_end(remove_btn, False, False, 0)
        
        return row
    
    def _on_bookmarks_clicked(self, button):
        """Show bookmarks popover"""
        popover = Gtk.Popover(relative_to=self.bookmarks_button)
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        box.set_margin_start(5)
        box.set_margin_end(5)
        box.set_margin_top(5)
        box.set_margin_bottom(5)
        
        # Add "Add Bookmark" button at the top
        add_button = Gtk.ModelButton(label="Add Current Page")
        add_button.connect("clicked", self._on_add_bookmark)
        box.pack_start(add_button, False, False, 0)
        
        box.pack_start(Gtk.Separator(), False, False, 5)
        
        # Display bookmarks
        bookmarks = self.storage._load_bookmarks()
        if bookmarks:
            for bookmark in bookmarks:
                row = self._create_bookmark_row(bookmark)
                box.pack_start(row, False, False, 0)
        else:
            label = Gtk.Label(label="No bookmarks yet")
            box.pack_start(label, False, False, 0)
        
        box.show_all()
        popover.add(box)
        popover.popup()
    
    def _on_add_bookmark(self, button):
        """Add current page to bookmarks"""
        # Get current page title and URL from the browser window
        if hasattr(self.window, 'webview'):
            title = self.window.webview.get_title() or "Untitled"
            url = self.window.webview.get_uri()
            if url:
                self.storage.add_bookmark(title, url)
    
    def _on_remove_bookmark(self, button, url):
        """Remove bookmark and refresh the popover"""
        self.storage.remove_bookmark(url)
        button.get_parent().get_parent().get_parent().popdown()  # Close the popover
        self._on_bookmarks_clicked(self.bookmarks_button)  # Reopen with updated list
    
    def _on_bookmark_clicked(self, button, url):
        """Load the bookmarked URL"""
        if hasattr(self.window, 'webview'):
            self.window.webview.load_uri(url)
            button.get_parent().get_parent().get_parent().popdown()  # Close the popover