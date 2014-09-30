import pyglet, random, math
from pyglet.window import key
from game import resources, cell, util, rectangle, load

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):

        # Core Functionality
        self.dimensions = util.get_dimensions()
        self.Width = self.dimensions[0]/2
        self.Height = self.dimensions[1]/2
        super(Window, self).__init__(self.Width,
                                     self.Height,
                                     caption='RandomWalk Version 1.0',
                                     resizable=True)

        self.batch = pyglet.graphics.Batch()
        self.pause = False
        self.num_cells = 100
        self.game_box = [(self.Width/5)+1,
                         0,
                         self.Width,
                         self.Height]
        self.game_objects = load.cells(self.game_box, self.num_cells, self.batch)

        # Pushing event handler to stack
        self.key_handler = key.KeyStateHandler()
        self.event_handler = self.key_handler
        self.push_handlers(self.event_handler)

        # Cosmetics

        self.Fullscreen = False
        #self.label = pyglet.text.Label(text = "Random Walk Version 1.0",
        #                         anchor_x = 'center',
        #                         x = self.Width / 2,
        #                         y = self.Height - 20,
        #                         batch = self.batch)

        # Prints
        print "Dimensions: ", self.dimensions[0],"x", self.dimensions[1]

    def on_draw(self):
            self.clear() #clears the screen
            rect = rectangle.Rectangle(0, 0, self.Width/5, self.Height, self.batch)
            self.batch.draw()


    def on_mouse_press(self, x, y, button, modifiers):
        clicked = False
        for obj in self.game_objects:
            if obj.hit_test(x, y):
                print obj.name
                print obj.scale
                clicked = True
                break

        if clicked == False:
            print "Click"

    def update(self, dt):

        # TODO: Encapsulate keyboard handling into separate methods
        if self.key_handler[key.SPACE]:
            self.pause = not self.pause

        if self.pause == True:
            return

        for obj in self.game_objects:
            obj.update(dt)


        for i in xrange(len(self.game_objects)):
            for j in xrange(i+1, len(self.game_objects)):
                obj_1 = self.game_objects[i]
                obj_2 = self.game_objects[j]
                #if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)

            if self.key_handler[key.P] and self.fullscreen == False:
                self.fullscreen = True
                self.set_fullscreen()
                pyglet.gl.glScalef(2.0, 2.0, 2.0)
                pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
                pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
            if self.key_handler[key.O] and self.fullscreen == True:
                self.fullscreen = False
                self.set_fullscreen(fullscreen=False)
                pyglet.gl.glScalef(0.5, 0.5, 0.5)
                pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
                pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MIN_FILTER, pyglet.gl.GL_NEAREST)
