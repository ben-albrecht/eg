import pyglet, random
from game import physicalobject, resources


class Matter(physicalobject.PhysicalObject):

    def __init__(self, name="Matter", scale=1.0, *args, **kwargs):

        super(Matter, self).__init__(img=resources.cell_image, *args, **kwargs)
        self._set_color((25+random.randint(-25, 25), 155+random.randint(-50, 100), 25+random.randint(-25, 25)))
        self.scale = scale
        self.name = name
        self.step_size = 1
        self.scale_inv = 1.0/self.scale

    def move(self):
        """ Random Walk code"""

        if random.random() < self.scale_inv:
            if bool(random.getrandbits(1)):
                if bool(random.getrandbits(1)):
                    return (1, 0)
                else:
                    return (-1, 0)
            else:
                if bool(random.getrandbits(1)):
                    return (0, 1)
                else:
                    return (0, -1)
        else:
            return (0, 0)


    def update(self, dt):
        movement = self.move()
        self.dx = movement[0]
        self.dy = movement[1]
        self.set_position(self.x + self.dx, self.y + self.dy)
        super(Matter, self).update(dt)



    def hit_test(self, x, y):
        """ See if we go out of bounds """
        if x < self.x + self.image.width*self.scale/2 and \
            x > self.x - self.image.width*self.scale/2 and \
            y < self.y + self.image.height*self.scale/2 and \
            y > self.y - self.image.height*self.scale/2:
                return True
        else:
            return False


    def handle_collision_with(self, other_object):
        super(Matter, self).handle_collision_with(other_object)
        if "cell" in other_object.name:
            if self.scale < 0.2:
                self.dead = True
                print self.name, " eaten by ", other_object.name
            else:
                self.scale += -0.1

