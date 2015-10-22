#!/usr/bin/env python3
# encoding: utf-8

import pyglet
from pyglet import gl

window = pyglet.window.Window()

def main():
    """
    :returns: TODO

    """
    pyglet.app.run()

@window.event
def on_mouse_press(x, y, button, modifiers):
    #print('press', x, y)
    pass

@window.event
def on_mouse_release(x, y, button, modifiers):
    #print('release', x, y)
    pass

@window.event
def on_mouse_drag(x, y, dx, dy, button, modifiers):
    #print('drag', x, y)
    print('box area', x*, y*dy)
    pass

if __name__ == '__main__':
    main()
