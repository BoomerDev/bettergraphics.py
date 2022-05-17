# Import required modules
import math

# Basic Vector2 class

class Vector2:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    # Overload math operators
    def __div__(self, what):
        if isinstance(what, Vector2):
            self.x /= what.x
            self.y /= what.y
        else:
            self.x /= what
            self.y /= what

    def get_normalized(self):
        v = self
        l = v.length()

        if v != 0:
            v /= l

        return v

    def get_as_list(self):
        return [self.x, self.y]

    def get_as_tuple(self):
        return (self.x, self.y)

class Color:
    r,g,b = 0,0,0

    def __init__(self, r, g, b):
        self.r, self.g, self.b = r, g, b

    def get_as_tuple(self):
        return (self.r, self.g, self.b)

    def get_as_html(self):
        return "#{:02x}{:02x}{:02x}".format(*self.get_as_tuple())
