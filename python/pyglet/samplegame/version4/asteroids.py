import pyglet, random, math
from game import load, resources, physicalobject, player
from game import resources
from game import physicalobject
from game import player

# Initialize Window, 800x600
game_window = pyglet.window.Window(800, 600)
# Main_batch for quickly drawing objects together at once
main_batch = pyglet.graphics.Batch()

# Label score and name of game
score_label = pyglet.text.Label(text="Score: 0",
                                x=10,
                                y=575,
                                batch=main_batch)

level_label = pyglet.text.Label(text="Asteroid Game",
                                      x=400, 
                                      y=575,
                                      anchor_x='center',
                                      batch=main_batch)

# Instantiate player ship object, Load lives, and asteroids
player_ship = player.Player(x=400, y=300, batch=main_batch)
player_lives = load.player_lives(player_ship.lives, main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)

# Create list of object in game for update() every frame
game_objects = [player_ship] + asteroids

#game_window.push_handlers(player_ship.key_handler)
for obj in game_objects:
   for handler in obj.event_handlers:
       game_window.push_handlers(handler)

@game_window.event
def on_draw():
    """ Clear window and draw all of batch """
    game_window.clear()
    main_batch.draw()
    
        
def update(dt):
    """ 
    Update game for a given time step:
        Adding objects, collisions, removing objects
    """
    # Check for collisions, and handle them
    for i in xrange(len(game_objects)):
        for j in xrange(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

    # Initialize list, to_add
    to_add = []

    # Call obj.update() and check for obj.new_object per game object
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []


    # Remove any objects that died from game_objects and call obj.delete()
    # If dying object is adding new objects, add them here as well
    for to_remove in [obj for obj in game_objects if obj.dead]:
        to_add.extend(obj.new_objects)
        to_remove.delete()
        game_objects.remove(to_remove)

    # Add objects to be added
    game_objects.extend(to_add) 


def debug(dt):
    """ Debugger function """
    for obj in game_objects:
        print obj.name
    print "------------------"


if __name__ == '__main__':
    # Update 120 times per second (twice as fast as common monitor refresh rate of 60 Hz)
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()

