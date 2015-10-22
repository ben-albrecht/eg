#!/usr/bin/env python3

import pyglet

win = pyglet.window.Window()

vertex_lists = []

@win.event
def on_resize(width, height):
    print(width, height)


@win.event
def on_draw():
    win.clear()

    for vertex_list in vertex_lists:
        vertex_list.draw(pyglet.gl.GL_TRIANGLES)



@win.event
def on_mouse_press(x, y, button, modifiers):
    global X, Y
    X = x
    Y = y
    print(x,y)


@win.event
def on_mouse_release(x, y, button, modifiers):
    global X
    global Y
    if abs(X-x) > 5 or abs(Y-y) > 5:
        print('drag')
        vertex_lists.append(pyglet.graphics.vertex_list(2,
                            ('v3f', (X, Y, x, Y, (x-X)/2, y)),
                            ('c3B', (0, 0, 255, 0, 255, 0))
                           ))
    else:
        print('press')


#
#@win.event
#def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
#    vertex_lists.append(pyglet.graphics.vertex_list(2,
#                        ('v2i', (x, y, x+dx, y+dy)),
#                        ('c3B', (0, 0, 255, 0, 255, 0))
#                       ))
#
def main():

    # Attaching event to window that will be recognized by event dispatcher
    pyglet.app.run()

if __name__ == '__main__':
    main()
