import pyglet
import random
from game import cell

def cells(box, num_cells, Batch):
    # box[x1,y1, x2, y2]

    cell_counter = 0
    cells = []
    # TODO: There is definitely a more efficient way to doing this
    while cell_counter < num_cells:
        newcell = cell.Cell(box=box,
                            scale=random.randint(5,20)*0.1,
                            name="Cell_"+str(cell_counter),
                            x=random.randint(box[0], box[2]),
                            y=random.randint(box[1], box[3]),
                            batch=Batch)
        collides = False
        for i in xrange(len(cells)):
            other_cell = cells[i]
            if newcell.collides_with(other_cell):
                collides = True
                break
        if not collides:
            newcell._set_color((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
            cells.append(newcell)
            cell_counter += 1



    
    return cells
