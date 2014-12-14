import pyglet
import physicalobject, resources

class Bullet(physicalobject.PhysicalObject):
    """ Bullets fired by player """

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(resources.bullet_image, *args, **kwargs)
        # Tell  bullet to die after 0.5 seconds
        pyglet.clock.schedule_once(self.die, 0.5)

        self.is_bullet = True


    def die(self, dt):
        self.dead = True
