import pyglet
from game import load
from game import resources
from game import physicalobject
from game import player

# Set resources path
pyglet.resource.path = ['../resources']

# Not sure what this does right now
# I assume it indexes and saves to memory the name of resource files
pyglet.resource.reindex()

# Initializes 800x600 windows
game_window = pyglet.window.Window(800, 600)

# Create batch - anything part of this batch will be drawn via the on_draw function
# We don't want to use batches to update already drawn objects' positions though
# For that, we use a game_object list and update functions
main_batch = pyglet.graphics.Batch()

# Generate score label at top of screen
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)

# Generate name of game at top of window
level_label = pyglet.text.Label(text="Ben's Asteroid Game",
                                      x=400, y=575, anchor_x='center', batch=main_batch)

# Generate player ship 
player_ship = player.Player(x=400, y=300, batch=main_batch)

# generate player lives at top right of screen
player_lives = load.player_lives(3, main_batch)

# generate asteroids at start of game
asteroids = load.asteroids(3, player_ship.position, main_batch)

# Create list of object in game to update each frame
game_objects = [player_ship] + asteroids

# Tell pyglet that player_ship is an event handler
# Question - What is an event handler?
# Well, this is pushing player_ship into the event stack
game_window.push_handlers(player_ship)


@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()
    
        
def update(dt):
    for obj in game_objects:
        obj.update(dt)





if __name__ == '__main__':

    # Update 120 times per second (twice as fast as common monitor refresh rate of 60 Hz)
    pyglet.clock.schedule_interval(update, 1/120.0)

    pyglet.app.run()



