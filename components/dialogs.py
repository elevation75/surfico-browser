import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

def show_about_dialog(window):
    """Show about dialog with program icon"""
    about_dialog = Gtk.AboutDialog(transient_for=window, modal=True)
    
    # Set the program icon
    icon = Gtk.Image.new_from_icon_name("web-browser", Gtk.IconSize.DIALOG)
    about_dialog.set_logo(icon.get_pixbuf())
    
    about_dialog.set_program_name("Surfico Browser")
    about_dialog.set_version("0.1")
    about_dialog.set_comments("First attempt to build my personal web browser helped by AI tools")
    about_dialog.set_website("https://github.com/elevation75/surfico-browser")
    about_dialog.run()
    about_dialog.destroy()
