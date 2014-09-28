import pyglet, random, math
from pyglet.window import key
from game import resources, cell, util

# TODO: Auto-Detect Display pixels (not same as resolution)
# macbookpro 13'' =1280x800
win_width = 640
win_height = 400
#display = pyglet.window.get_platform().get_default_display()
#screens = pyglet.display.get_screens()
win = pyglet.window.Window(win_width , win_height)
#win = pyglet.window.Window(fullscreen = True)

main_batch = pyglet.graphics.Batch()

win_label = pyglet.text.Label(text = "Random Walk Version 1.0",
                                 anchor_x = 'center',
                                 x = win_width / 2,
                                 y = win_height - 20,
                                 batch = main_batch)


Cell_1 = cell.Cell(x=win_width/2, y=win_height/2, batch=main_batch)
key_handler = key.KeyStateHandler()
event_handler = key_handler
win.push_handlers(event_handler)
fullscreen = False

game_objects = [Cell_1]

@win.event
def on_draw():
        win.clear() #clears the screen
        main_batch.draw()

@win.event
def update(dt):
    global fullscreen

    for obj in game_objects:
        obj.update(dt)

    if key_handler[key.P] and fullscreen == False:
        fullscreen = True
        win.set_fullscreen()
        pyglet.gl.glScalef(2.0, 2.0, 2.0)
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
    if key_handler[key.O] and fullscreen == True:
        fullscreen = False
        win.set_fullscreen(fullscreen=False)
        pyglet.gl.glScalef(0.5, 0.5, 0.5)
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST) 
        pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)



if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
