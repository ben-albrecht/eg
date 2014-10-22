import pyglet
from pyglet.gl import *
from pyglet.window import Window
platform = pyglet.window.get_platform()
display = platform.get_default_display()
screens = display.get_screens()
#  screen_id = 0 - first monitor (primary)
#  screen_id = 1 - second monitor
screen_id = 1
window = Window(fullscreen=True, screen=screens[screen_id])
glClearColor(0.2, 0.2, 0.2, 1.0)
@window.event
def on_draw():
    window.clear()
    glClear(GL_COLOR_BUFFER_BIT)
pyglet.app.run()
