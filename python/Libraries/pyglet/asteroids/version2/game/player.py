import math
from pyglet.window import key
import physicalobject, resources

class Player(physicalobject.PhysicalObject):
    """Class for player, subclass of PhysicalObject """

    def __init__(self, *args, **kwargs):
        # super is a constructor allowing for avoidance of 
        #   explicitly referencing the base class, which is nice for
        #   multiple inheritance, like this case
        super(Player, self).__init__(img=resources.player_image, *args, **kwargs)

        self.thrust = 300.0
        self.rotate_speed = 200.0

        # Dictionary to determine what state each key is in
        self.keys = dict(left=False, right=False, up=False)

    # Sloppy, but pedagogical way of doing this
    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True


    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False


    def update(self, dt):
        # Call inherited class function first
        super(Player, self).update(dt)

        # Note rotation is in units of degrees (/360)
        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt
        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y



