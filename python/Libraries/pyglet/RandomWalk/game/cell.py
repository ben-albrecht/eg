import pyglet, random
from game import resources, physicalobject, matter

class Cell(physicalobject.PhysicalObject):

    def __init__(self, scale=1.0, name="Cell", *args, **kwargs):

        super(Cell, self).__init__(img=resources.cell_image, *args, **kwargs)
        self.scale = scale
        self.name = name
        self.step_size = 1
        self.scale_inv = 1.0/self.scale
        self._set_color((192+random.randint(-80,10), 192+random.randint(-40, 20), 192+random.randint(-10, 50)))
        self.energy = 100

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
        if self.energy >= 150:
            self.spawn()
        else:
            movement = self.move()
            self.dx = movement[0]
            self.dy = movement[1]
            self.set_position(self.x + self.dx, self.y + self.dy)
            super(Cell, self).update(dt)
            
            self.energy += self.energy_decay()



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
        super(Cell, self).handle_collision_with(other_object)
        if "matter" in other_object.name:
            self.energy += other_object.scale*10
            pass

        
    def spawn(self):
        print self.name, "spawns new offspring!"
        self.energy += -self.energy/2

    def energy_decay(self):
        if random.randint(0,5) == 0:
            return -1
        else:
            return 0


