# BetterGraphics.py

BetterGraphics.py is a new and improved version of the old 'graphics.py' pip module. It aims to be more performant and object-oriented.

```py
# Boilerplate code
from bettergraphics import *

# Create window with the title "Test Window" and the size of (640, 480)
win = Window("Test Window", Vector2(640, 480))
```

## Creating objects
```py

# Create rectangle object with a base and height of 100, and set the position to the center of the window
square = Rectangle(win, 100, 100, win.center)

# Set the outline color to red
square.outline_color = Color(255, 0, 0)

# Set the fill color to blue
square.fill_color = Color(0, 255, 0)

# Add the square to the canvas
square.instantiate()
```
