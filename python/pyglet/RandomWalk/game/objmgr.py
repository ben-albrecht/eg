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

        #matter_counter = 0 
        #num_matter = 10
        #while matter_counter < num_matter:
        #    newmatter = matter.Matter(box=box,
        #                        scale=random.randint(3,10)*0.1,
        #                        name="Matter_"+str(matter_counter),
        #                        x=random.randint(box[0], box[2]),
        #                        y=random.randint(box[1], box[3]),
        #                        batch=Batch)
        #    collides = False
        #    for i in xrange(len(cells)):
        #        other_cell = cells[i]
        #        if newmatter.collides_with(other_cell):
        #            collides = True
        #            break
        #    if not collides:
        #        cells.append(newmatter)
        #        matter_counter += 1
    
    
    
        
