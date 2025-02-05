import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

class MenuButton(Gtk.Box):
    def __init__(self, window):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.window = window
        self._create_menu_button()
        self._create_menu()
        self._add_menu_items()
        
    def _create_menu_button(self):
        """Create and configure the menu button"""
        self.menu_button = Gtk.MenuButton()
        self.menu_button.set_relief(Gtk.ReliefStyle.NONE)
        hamburger_icon = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.MENU)
        self.menu_button.set_image(hamburger_icon)
        self.pack_start(self.menu_button, False, False, 0)
        
    def _create_menu(self):
        """Create the popover menu and its container"""
        self.menu = Gtk.PopoverMenu()
        self.menu_button.set_popover(self.menu)
        
        self.menu_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        for side in ['start', 'end', 'top', 'bottom']:
            setattr(self.menu_box, f'set_margin_{side}', 5)
            
    def _add_menu_items(self):
        """Add all menu items to the menu"""
        menu_items = [
            ("About", self._on_about_clicked),
            ("Help", self._on_help_clicked),
            (None, None),  # Separator
            ("Extensions", self._on_extensions_clicked)
        ]
        
        for label, handler in menu_items:
            if label is None:
                self.menu_box.pack_start(Gtk.Separator(), False, False, 5)
                continue
                
            button = Gtk.ModelButton(label=label)
            if handler:
                button.connect("clicked", handler)
            self.menu_box.pack_start(button, False, False, 5)
            
        self.menu_box.show_all()
        self.menu.add(self.menu_box)
        
    def _on_about_clicked(self, button):
        """Show about dialog with program icon"""
        about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        
        # Set the program icon
        # Set the custom program icon
        logo = GdkPixbuf.Pixbuf.new_from_file("/home/just/Documents/idei/waybar-idei/browser/surfico-logo.png")
        about_dialog.set_logo(logo)
        
        about_dialog.set_program_name("Surfico Browser")
        about_dialog.set_version("0.1")
        about_dialog.set_comments("First attempt to build my personal web browser helped by AI tools")
        about_dialog.set_website("https://github.com/yourusername/surfme")
        about_dialog.run()
        about_dialog.destroy()
    
    def _on_help_clicked(self, button):
        """Show help (to be implemented)"""
        pass
    
    def _on_extensions_clicked(self, button):
        """Show extensions manager (to be implemented)"""
        pass