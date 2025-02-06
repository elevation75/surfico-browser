import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf
from bookmarks_button import BookmarksButton

class MenuButton(Gtk.Box):
    def __init__(self, window):
        Gtk.Box.__init__(self, orientation=Gtk.Orientation.HORIZONTAL)
        self.window = window
        self.logo_path = "surfico-logo.png"
        
        # Create bookmarks button
        self.bookmarks_button = BookmarksButton(window)
        self.pack_start(self.bookmarks_button, False, False, 0)

        # Create menu button
        self.menu_button = Gtk.MenuButton()
        self.menu_button.set_relief(Gtk.ReliefStyle.NONE)
        hamburger_icon = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.MENU)
        self.menu_button.set_image(hamburger_icon)
        
        # Create popover menu
        self.menu = Gtk.PopoverMenu()
        self.menu_button.set_popover(self.menu)
        
        # Create menu box
        menu_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        menu_box.set_margin_start(5)
        menu_box.set_margin_end(5)
        menu_box.set_margin_top(5)
        menu_box.set_margin_bottom(5)
        
        # Add menu items
        about_button = Gtk.ModelButton(label="About")
        about_button.connect("clicked", self._on_about_clicked)
        
        help_button = Gtk.ModelButton(label="Help")
        help_button.connect("clicked", self._on_help_clicked)
        
        extensions_button = Gtk.ModelButton(label="Extensions")
        extensions_button.connect("clicked", self._on_extensions_clicked)
        
        # Pack menu items
        menu_box.pack_start(about_button, False, False, 5)
        menu_box.pack_start(help_button, False, False, 5)
        menu_box.pack_start(Gtk.Separator(), False, False, 5)
        menu_box.pack_start(extensions_button, False, False, 5)
        
        menu_box.show_all()
        self.menu.add(menu_box)
        
        # Pack menu button
        self.pack_start(self.menu_button, False, False, 0)
    
    def _on_about_clicked(self, button):
        """Show about dialog with program icon"""
        about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        
        # Set the custom program icon
        logo = GdkPixbuf.Pixbuf.new_from_file(self.logo_path)
        about_dialog.set_logo(logo)
        about_dialog.set_program_name("Surfico Browser")
        about_dialog.set_version("build ver.0.1")
        about_dialog.set_comments("First attempt to build my personal web browser helped by AI tools")
        about_dialog.set_website("https://github.com/elevation75/surfico-browser")
        about_dialog.set_copyright("Surfico logo and names are trademarks registered of Surfico Foundation")
        about_dialog.run()
        about_dialog.destroy()
    
    def _on_help_clicked(self, button):
        """Show help dialog"""
        help_dialog = Gtk.Dialog(
            title="Help",
            transient_for=self.window,
            modal=True
        )
        
        # Add content area
        content_area = help_dialog.get_content_area()
        content_area.set_margin_start(10)
        content_area.set_margin_end(10)
        content_area.set_margin_top(10)
        content_area.set_margin_bottom(10)
        content_area.set_spacing(10)
        
        # Add logo at the top
        logo = GdkPixbuf.Pixbuf.new_from_file(self.logo_path)
        logo_image = Gtk.Image.new_from_pixbuf(logo)
        content_area.pack_start(logo_image, False, False, 0)

        # Add a separator
        separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
    
        # Apply custom CSS to the separator
        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
            separator {
                color: #e32b7a;
                background-color: #e32b7a;
            }
        """)
        context = separator.get_style_context()
        context.add_provider(css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
    
        content_area.pack_start(separator, False, False, 10)

        # Add help text
        help_text = Gtk.Label()
        help_text.set_markup(
            "<b>Welcome to Surfico Browser!</b>\n\n"
            "This is a simple web browser built with Python and GTK and with AI tools guidance.\n\n"
            "Features:\n"
            "• Basic web navigation\n"
            "• Bookmarks support\n"
            "• History tracking\n\n"
            "• Extensions support (in future builds)\n\n"
            "For more information and updates, visit our "
            "<a href='https://github.com/elevation75/surfico-browser'>GitHub repository</a>"
        )
        help_text.set_use_markup(True)
        help_text.set_line_wrap(True)
        help_text.set_selectable(True)
        content_area.pack_start(help_text, True, True, 0)
        
        # Add second separator
        separator2 = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        context2 = separator2.get_style_context()
        context2.add_provider(css_provider, Gtk.STYLE_PROVIDER_PRIORITY_USER)
        content_area.pack_start(separator2, False, False, 10)

        # Add close button
        help_dialog.add_button("Close", Gtk.ResponseType.CLOSE)
        
        help_dialog.show_all()
        help_dialog.run()
        help_dialog.destroy()
    
    def _on_extensions_clicked(self, button):
        """Show extensions manager (to be implemented)"""
        pass