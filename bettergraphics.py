# Import local types
from bettergraphics_types import *

# Standard platform specific import
try:
    import tkinter as tk
except ImportError:
    import Tkinter as tk

class Window:
    def __init__(self, title, size_vec2):
        self._thiswin = tk.Tk()
        self._thiscanvas = tk.Canvas(self._thiswin, width=size_vec2.x, height=size_vec2.y)

        self._thiscanvas.pack()

        self.size = size_vec2
        self.center = Vector2(size_vec2.x / 2, size_vec2.y / 2)
        
        if title.strip() == "":
            self._thiswin.title("Better Graphics Window")
        else:
            self._thiswin.title(title)

        self._thiswin.geometry("%dx%d" % (size_vec2.x, size_vec2.y))

class BetterGraphicsObjectBase:
    outline_color = Color(0, 0, 0)
    fill_color = Color(1, 1, 1)

    def instantiate(self):
        pass

class Rectangle(BetterGraphicsObjectBase):
    def __init__(self, window, base, height, center_vec2):
        self.window = window
        self.base = base
        self.height = height
        self.center_vec2 = center_vec2

    def instantiate(self):
        top_left = Vector2(self.center_vec2.x - self.base, self.center_vec2.y - self.height)
        bottom_right = Vector2(self.center_vec2.x + self.base, self.center_vec2.y + self.height)

        self.window._thiscanvas.create_rectangle(top_left.x, top_left.y, bottom_right.x, bottom_right.y, outline=self.outline_color.get_as_html(), fill=self.fill_color.get_as_html())

class Circle(BetterGraphicsObjectBase):
    def __init__(self, window, radius, center_vec2):
        self.window = window
        self.radius = radius
        self.center_vec2 = center_vec2

    
    def instantiate(self):
        px = Vector2(self.center_vec2.x - self.radius, self.center_vec2.y - self.radius)
        py = Vector2(self.center_vec2.x + self.radius, self.center_vec2.y + self.radius)

        self.window._thiscanvas.create_oval(px.x, px.y, py.x, py.y)
