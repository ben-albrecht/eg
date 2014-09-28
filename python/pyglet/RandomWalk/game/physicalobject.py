import pyglet
from game import resources, util

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super(PhysicalObject, self).__init__(*args, **kwargs) 



    def check_bounds(self):
        """
        Check boundaries of window
        """
        pass 
