import pyglet
import random
from game import cell, matter

class ObjMgr():
    """
    Class to add new objects into game window
    that do not spawn from other game objects
    """
    def __init__(self, box,  Batch):
        """
        Inialized with a running list of game_objects
        """
        self.box = box
        self.xmin = box[0]
        self.ymin = box[1]
        self.xmax = box[2]
        self.ymax = box[3]
        self.Batch = Batch
        # Counters
        self.counter_type = []
        self.counter = [0, 0]
        # game_objects
        self.game_objects = []

        self.types = {'cell'   : cell.Cell,
                      'matter' : matter.Matter}

        self.indices = {'cell'   : 0,
                         'matter' : 1}


    def update(self, dt):
        pass


    def load(self, Type='cell', Num=10):
        #for i in len(self.counter_type):
        #if not any(Type in s for s in self.counter_type):
        # Check if Type is already in counter list
        #self.counter.append(0) 

        while self.counter[self.indices[Type]] < Num:
            new_obj = self.types[Type](box=self.box,
                                scale=random.randint(5,20)*0.1,
                                name=Type+str(self.counter[self.indices[Type]]),
                                x=random.randint(self.xmin, self.xmax),
                                y=random.randint(self.ymin, self.ymax),
                                batch=self.Batch)
    
            collides = False
            for i in xrange(len(self.game_objects)):
                other_obj = self.game_objects[i]
                if new_obj.collides_with(other_obj):
                    collides = True
                    break
            if not collides:
                self.game_objects.append(new_obj)
                self.counter[self.indices[Type]] += 1
    
        return self.game_objects

    
    def update(self, dt): 
        # Efficiency: 
        # (1) Only if an object is in self.has_moved[ ] will they check collision
        # (2) Chop up game window into grid, and only check collisions with grid
        
        for i in xrange(len(self.game_objects)):
            for j in xrange(i+1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                if not obj_1.dead and not obj_2.dead:
                    if obj_1.collides_with(obj_2):
                        obj_1.handle_collision_with(obj_2)
                        obj_2.handle_collision_with(obj_1)

        # Start list of objects to add
        #to_add = []

        # Update every object
        for obj in self.game_objects:
            obj.update(dt)
            #to_add.extend(obj.new_objects)
            #obj.new_objects = []

        # Remove any objects that died from game_objects and call obj.delete()
        # If dying object is adding new objects, add them here as well
        for to_remove in [obj for obj in self.game_objects if obj.dead]:
        #    to_add.extend(obj.new_objects)
             to_remove.delete()
             self.game_objects.remove(to_remove)

        ## Add objects to be added
        #self.game_objects.extend(to_add)
