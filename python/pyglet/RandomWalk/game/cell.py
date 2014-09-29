import pyglet
import random
from game import resources, physicalobject

class Cell(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super(Cell, self).__init__(img=resources.cell_image, *args, **kwargs)
        self.step_size = 1
        self.name = "Cell"


    def update(self, dt):
        axis = random.randint(0,1)
        direction = random.randint(0,1)
        if axis == 0:
            if direction == 0:
                self.x += self.step_size
            else:
                self.x += -self.step_size
        else:
            if direction == 0:
                self.y += self.step_size
            else:
                self.y += -self.step_size
        super(Cell, self).update(dt)


    def hit_test(self, x, y):
        if x < self.x + self.image.width/2 and \
            x > self.x - self.image.width/2 and \
            y < self.y + self.image.height/2 and \
            y > self.y - self.image.height/2:
                return True
        else:
            return False

