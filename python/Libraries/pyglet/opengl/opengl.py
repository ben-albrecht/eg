#!/usr/bin/env python3

import pyglet
from pyglet import gl
window = pyglet.window.Window()

gl.glClearColor(0.2, 0.4, 0.5, 1.0)

vertices = []
size = 50

@window.event
def on_draw():
    global vertices
    gl.glClear(gl.GL_COLOR_BUFFER_BIT)

    gl.glColor3f(0, 0, 0)

    gl.glBegin(gl.GL_TRIANGLES)
    for vertex in vertices:
        gl.glVertex2f(*vertex)

    gl.glEnd()

@window.event
def on_mouse_press(x, y, button, modifiers):
    global size
    if button == pyglet.window.mouse.RIGHT:
        global vertices
        vertices = []
        size = 50
    else:
        draw_triangle(x, y, size=size)
        size /= 1.1


def draw_triangle(x, y, size=50):
    global vertices
    vertices.append((x, y+size))
    vertices.append((x+size, y-size))
    vertices.append((x-size, y-size))


pyglet.app.run()
