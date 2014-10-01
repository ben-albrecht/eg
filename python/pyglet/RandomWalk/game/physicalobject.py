import pyglet
from game import resources, util

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, box=[1920, 1080], name="physical object", *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        # Eventually I'll make a window class with shared memory for physical objects to access
        #self.dimensions = [1920, 1080]

        self.min_x = box[0] + self.image.width/2
        self.min_y = box[1] + self.image.height/2

        self.max_x = box[2] - self.image.width/2
        self.max_y = box[3] - self.image.height/2
        self.dx = 0
        self.dy = 0
        self.scale = 1.0
        self.dead = False


    def check_bounds(self):
        """
        Check boundaries of window
        """
        if self.x < self.min_x:
            self.x = self.min_x
        elif self.x > self.max_x:
            self.x = self.max_x
        if self.y < self.min_y:
            self.y = self.min_y
        elif self.y > self.max_y:
            self.y = self.max_y


    def collides_with(self, other_object):
        collision_distance = (self.image.width / 2)*self.scale + self.scale * other_object.image.width / 2
        actual_distance = util.distance(self.position, other_object.position)
        return (actual_distance <= collision_distance)


    # Maybe handle collisions within each specific class?
    def handle_collision_with(self, other_object):
        if other_object.__class__ == self.__class__:
            # Bounce away
            if self.x <= other_object.x:
                dx = -1
            else:
                dx = 1
            if self.y <= other_object.y:
                dy = -1
            else:
                dy = 1
            self.set_position(self.x + dx, self.y + dy)
            other_object.set_position(other_object.x + dx, other_object.y + dy)
        else:
            pass


    def update(self, dt):
       self.check_bounds()

    
    def delete(self):
        """ Delete object"""
        #self.engine_sprite.delete() 
        super(PhysicalObject, self).delete()



