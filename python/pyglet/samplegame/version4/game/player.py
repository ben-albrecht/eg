import math
from pyglet.window import key
import pyglet
# TODO: How can I import JUST pyglet.sprite ?
import physicalobject, resources, bullet


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
        self.bullet_speed = 700.0

        self.react_to_bullets = False

        # Dictionary to determine what state each key is in
        #  self.keys = dict(left=False, right=False, up=False)
        # Manages states of keys, rather than manually
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]



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

        if self.key_handler[key.SPACE]:
            self.fire()



        

#    def on_key_press(self, symbol, modifiers):
#        if symbol == key.SPACE:
#            self.fire()


    def fire(self):
        """
        The complicated fire function
        """
        # convert rotation angle to radians
        angle_radians = -math.radians(self.rotation)
        # Circumference of ship/2 = radius
        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)

        bullet_vx = (self.velocity_x + math.cos(angle_radians) * self.bullet_speed)
        bullet_vy = (self.velocity_y + math.sin(angle_radians) * self.bullet_speed)

        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy

        self.new_objects.append(new_bullet)


    def delete(self):
        # Remove engine sprite, unique to the subclass
        # self.engine_sprite.visible = False
        self.engine_sprite.delete()
        # Call delete function of superclass to remove other game objects of player
        super(Player, self).delete()
