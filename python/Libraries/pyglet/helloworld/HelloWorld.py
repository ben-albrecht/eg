#!/usr/bin/env python

import pyglet

# create window with default constructor -> visibile immediately, and auto-determine parameters
window = pyglet.window.Window()

# create label for text
label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

# attach event handler via decorator
@window.event
def on_draw():
    window.clear()
    label.draw()


pyglet.app.run()




