import pyglet
from game import resources, util

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, name="physical object", *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs)
        self.name = name



    def check_bounds(self):
        """
        Check boundaries of window
        """
        win_width = 640
        win_height = 400
        min_x = 82 + -self.image.width/2
        min_y = -self.image.height/2
        max_x = win_width + self.image.width/2
        max_y = win_height + self.image.width/2
        if self.x < min_x:
            self.x = min_x
        elif self.x > max_x:
            self.x = max_x
        if self.y < min_y:
            self.y = min_y
        elif self.y > max_y:
            self.y = max_y


    def update(self, dt):
       self.check_bounds()
