import pyglet
import random
import resources, physicalobject


class Asteroid(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        super(Asteroid, self).__init__(resources.asteroid_image, *args, **kwargs)

        self.rotate_speed = random.random() * 100.0 - 50
        self.name = "Asteroid"



    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        # Make new asteroids come out of old asteroids
        if self.dead and self.scale > 0.25:
            # 2-3 new asteroids
            num_asteroids = random.randint(2, 3)
            # Generate new roation, velocity and size for new asteroids
            for i in xrange(num_asteroids):
                new_asteroid = Asteroid(x=self.x + random.randint(-10, 10),
                        y=self.y + random.randint(-10, 10),
                        batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = random.random() * 70 + self.velocity_x
                new_asteroid.velocity_y = random.random() * 70 + self.velocity_y
                new_asteroid.scale = self.scale * 0.5
                self.new_objects.append(new_asteroid)


    # New asteroids will rotate faster
    def update(self, dt):
        super(Asteroid, self).update(dt)
        self.rotation += self.rotate_speed * dt
