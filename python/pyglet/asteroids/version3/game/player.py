import math
from pyglet.window import key
import pyglet
# TODO: How can I import JUST pyglet.sprite ?
import physicalobject, resources

class Player(physicalobject.PhysicalObject):
    """Class for player, subclass of PhysicalObject """

    def __init__(self, *args, **kwargs):
        # super is a constructor allowing for avoidance of 
        #   explicitly referencing the base class, which is nice for
        #   multiple inheritance, like this case
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        # Initialize engine_image
        # Set engine flame initially invisible
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False

        self.thrust = 300.0
        self.rotate_speed = 200.0

        # Dictionary to determine what state each key is in
        #  self.keys = dict(left=False, right=False, up=False)
        # Manages states of keys, rather than manually
        self.key_handler = key.KeyStateHandler()



    def update(self, dt):
        # Call inherited class function first
        super(Player, self).update(dt)

        # Note rotation is in units of degrees (/360)
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            # Engine flame
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False


    def delete(self):
        # Remove engine sprite, unique to the subclass
        # self.engine_sprite.visible = False
        self.engine_sprite.delete()
        # Call delete function of superclass to remove other game objects of player
        super(Player, self).delete()
        
