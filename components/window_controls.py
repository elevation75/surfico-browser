import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from .menu_button import MenuButton

class WindowControls(Gtk.Box):
    def __init__(self, window):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
        
        # Create menu button
        self.menu_button = MenuButton(window)
        
        # Minimize button
        self.minimize_button = Gtk.Button()
        minimize_icon = Gtk.Image.new_from_icon_name("window-minimize", Gtk.IconSize.MENU)
        self.minimize_button.set_image(minimize_icon)
        self.minimize_button.set_relief(Gtk.ReliefStyle.NONE)
        self.minimize_button.connect("clicked", lambda w: window.iconify())
        
        # Maximize button
        self.maximize_button = Gtk.Button()
        self.maximize_icon = Gtk.Image.new_from_icon_name("window-maximize", Gtk.IconSize.MENU)
        self.restore_icon = Gtk.Image.new_from_icon_name("window-restore", Gtk.IconSize.MENU)
        self.maximize_button.set_image(self.maximize_icon)
        self.maximize_button.set_relief(Gtk.ReliefStyle.NONE)
        self.maximize_button.connect("clicked", self.on_maximize_clicked, window)
        
        # Close button
        self.close_button = Gtk.Button()
        close_icon = Gtk.Image.new_from_icon_name("window-close", Gtk.IconSize.MENU)
        self.close_button.set_image(close_icon)
        self.close_button.set_relief(Gtk.ReliefStyle.NONE)
        self.close_button.connect("clicked", lambda w: window.close())
        
        # Pack buttons
        self.pack_start(self.menu_button, False, False, 0)
        self.pack_start(self.minimize_button, False, False, 0)
        self.pack_start(self.maximize_button, False, False, 0)
        self.pack_start(self.close_button, False, False, 0)
        
        # Connect window state events
        window.connect("window-state-event", self.on_window_state_changed)
        
    def on_maximize_clicked(self, button, window):
        """Toggle between maximized and normal state"""
        if window.is_maximized():
            window.unmaximize()
        else:
            window.maximize()
    
    def on_window_state_changed(self, window, event):
        """Update maximize button icon based on window state"""
        if window.is_maximized():
            self.maximize_button.set_image(self.restore_icon)
        else:
            self.maximize_button.set_image(self.maximize_icon)