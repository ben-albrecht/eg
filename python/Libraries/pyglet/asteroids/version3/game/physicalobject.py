import pyglet
import util
#from util import distance

class PhysicalObject(pyglet.sprite.Sprite):


    def __init__(self, *args, **kwargs):
        """
        Initialize physical object, with properties of velocity
        """
        # Make PhysicalObject a subclass of Sprite
        super(PhysicalObject, self).__init__(*args, **kwargs)

        self.velocity_x, self.velocity_y =0.0, 0.0
        self.dead = False
        

    def update(self, dt):
        """
        Update position based on current velocity
        """
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        self.check_bounds()


    def check_bounds(self):
        """ 
        Check boundaries of game window,
        to make sure objects do not fly off screen
        Instead, they will loop to other side of window
        """
        min_x = -self.image.width/2
        min_y = -self.image.height/2
        max_x = 800 + self.image.width/2
        max_y = 600 + self.image.width/2
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y


    def collides_with(self, other_object):
        collision_distance = self.image.width / 2 + other_object.image.width / 2 
        actual_distance = util.distance(self.position, other_object.position) 
        return (actual_distance <= collision_distance)


    def handle_collision_with(self, other_object):
        self.dead = True
        pass

