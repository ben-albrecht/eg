import pyglet
from game import window

win = window.Window()

if __name__ == '__main__':
    pyglet.clock.schedule_interval(win.update, 1/120.0)
    pyglet.app.run()
