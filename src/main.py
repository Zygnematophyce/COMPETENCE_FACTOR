# coding: utf-8

# Using Gtk 3.0 library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import cairo

def draw_polygone(widget, cairo):
    """ Drawing polygone with cairo. """
    cairo.move_to(30, 30)
    cairo.line_to(30, 55)
    cairo.line_to(60, 55)
    cairo.line_to(30, 70)
    cairo.stroke_preserve()
    cairo.set_source_rgb(1, 0, 0)
    cairo.set_line_width(5)
    cairo.stroke()
    return False

if __name__ == "__main__":
    print("Competence factor")

    # Create window
    window = Gtk.Window()

    # Set title of window
    window.set_title("Competence Factor")

    # Set size of window
    window.set_size_request(400, 550)

    # Centering the window
    window.set_position(Gtk.WindowPosition.CENTER)

    # Add destroy button to quit window
    window.connect("destroy", Gtk.main_quit)

    # Create a drawing area
    drawing_area = Gtk.DrawingArea()

    # Add drawing area
    drawing_area.connect('draw', draw_polygone)

    # Add drawing area into the window
    window.add(drawing_area)

    # Show all
    window.show_all()

    # The window loop
    Gtk.main()
