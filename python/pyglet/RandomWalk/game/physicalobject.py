import pyglet
from game import resources, util

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, name="physical object", *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        # Eventually I'll make a window class with shared memory for physical objects to access
        self.dimensions = [1920, 1080]
        self.name = "cell"
        self.min_y = self.image.height/2
        self.max_y = self.dimensions[1]/2  - self.image.height/2
        self.min_x = self.dimensions[0]/10 + self.image.width/2
        self.max_x = self.dimensions[0]/2 - self.image.width/2


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


    def update(self, dt):
       self.check_bounds()
