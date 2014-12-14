import pyglet
from game import load
from game import resources

# Set resources path
pyglet.resource.path = ['../resources']
# Not sure what this does right now
pyglet.resource.reindex()

# Initializes 800x600 windows
game_window = pyglet.window.Window(800, 600)

score_label = pyglet.text.Label(text="Score: 0", x=10, y=575)
level_label = pyglet.text.Label(text="Ben's Asteroid Game",
                                      x=400, y=575, anchor_x='center')

player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)

asteroids = load.asteroids(3, player_ship.position)

@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()
    player_ship.draw()
    for asteroid in asteroids:
        asteroid.draw()

    
        














if __name__ == '__main__':
    pyglet.app.run()



