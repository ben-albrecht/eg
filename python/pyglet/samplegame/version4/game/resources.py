import pyglet
from game import util


pyglet.resource.path = ['../resources']
pyglet.resource.reindex()


player_image = pyglet.resource.image("player.png")
util.center_image(player_image)

bullet_image = pyglet.resource.image("bullet.png")
util.center_image(bullet_image)

asteroid_image = pyglet.resource.image("asteroid.png")
util.center_image(asteroid_image)

engine_image = pyglet.resource.image("engine_flame.png")

# Anchor points are the points in which the x,y coordinate are centered at
# We make this offset here, so that we can always set the engine coordinates
#   equal to that of the player_ship
engine_image.anchor_x = engine_image.width * 1.5
engine_image.anchor_y = engine_image.height / 2
