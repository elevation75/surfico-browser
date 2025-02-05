import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Pango

class TabLabel(Gtk.Box):
    def __init__(self, on_close_callback):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        
        # Create label with ellipsis support
        self.label = Gtk.Label(label="New Tab")
        self.label.set_ellipsize(Pango.EllipsizeMode.END)
        self.label.set_width_chars(20)
        self.label.set_max_width_chars(20)
        self.label.set_single_line_mode(True)
        self.pack_start(self.label, True, True, 0)
        
        # Create close button
        close_button = Gtk.Button.new_from_icon_name("window-close", Gtk.IconSize.MENU)
        close_button.connect("clicked", on_close_callback)
        close_button.set_relief(Gtk.ReliefStyle.NONE)
        self.pack_start(close_button, False, False, 0)
        
        self.show_all()
    
    def set_text(self, text):
        """Update the tab label text"""
        if not text:
            text = "New Tab"
        self.label.set_text(text)
        self.label.set_tooltip_text(text)