import pyglet
from game import util

pyglet.resource.path = ["./resources"]
pyglet.resource.reindex()

cell_image = pyglet.resource.image("cell.png")
util.center_image(cell_image)

