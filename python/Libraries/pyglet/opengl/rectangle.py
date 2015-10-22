import pyglet
import ctypes
import cairo

WIDTH = 800
HEIGHT = 600

window = pyglet.window.Window(width=WIDTH, height=HEIGHT)

#cairo
data = (ctypes.c_ubyte * WIDTH * HEIGHT * 4)()
stride = WIDTH * 4
surface = cairo.ImageSurface.create_for_data (data, cairo.FORMAT_RGB24, WIDTH, HEIGHT, stride);
ctx = cairo.Context(surface)
ctx.translate(200, 200)

#pyglet
texture = pyglet.image.Texture.create_for_size(pyglet.gl.GL_TEXTURE_2D, WIDTH, HEIGHT, pyglet.gl.GL_RGB)

@window.event
def on_draw():
    ctx.set_source_rgb(0, 1, 0)
    ctx.rectangle(5, 5, 50, 50)
    ctx.fill()
    
    window.clear()
    
    pyglet.gl.glEnable(pyglet.gl.GL_TEXTURE_2D)
    pyglet.gl.glBindTexture(pyglet.gl.GL_TEXTURE_2D, texture.id)
    
    pyglet.gl.glTexImage2D(pyglet.gl.GL_TEXTURE_2D, 0, pyglet.gl.GL_RGBA, WIDTH, HEIGHT, 1, pyglet.gl.GL_BGRA, pyglet.gl.GL_UNSIGNED_BYTE, data)
    
    pyglet.gl.glBegin(pyglet.gl.GL_QUADS)
    pyglet.gl.glTexCoord2f(0.0, 1.0)
    pyglet.gl.glVertex2i(0, 0)
    pyglet.gl.glTexCoord2f(1.0, 1.0)
    pyglet.gl.glVertex2i(WIDTH, 0)
    pyglet.gl.glTexCoord2f(1.0, 0.0)
    pyglet.gl.glVertex2i(WIDTH, HEIGHT)
    pyglet.gl.glTexCoord2f(0.0, 0.0)
    pyglet.gl.glVertex2i(0, HEIGHT)
    pyglet.gl.glEnd()
    
    ctx.set_source_rgb(0, 0, 0)
    ctx.paint()

pyglet.app.run()
