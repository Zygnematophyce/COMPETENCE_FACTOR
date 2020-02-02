# coding: utf-8

# using Gtk librairie
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from gi.repository import Gtk

if __name__ == "__main__":
    print("Competence factor")

    # Create windows
    window = Gtk.Window()

    # Add destroy button to quit window
    window.connect("destroy", Gtk.main_quit)

    # Show all
    window.show_all()

    # The window loop
    Gtk.main()
