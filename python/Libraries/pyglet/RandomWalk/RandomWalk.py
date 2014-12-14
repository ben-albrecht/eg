import pyglet
from game import window
import cProfile
import pstats


win = window.Window()

def main():
    pyglet.clock.schedule_interval(win.update, 1/60.0)
    pyglet.app.run()


if __name__ == '__main__':
    cProfile.run('main()', 'restats')
    p = pstats.Stats('restats')
    #p.strip_dirs().sort_stats(-1).print_stats()
    #p.strip_dirs().sort_stats('cumulative').print_stats(15)
    p.strip_dirs().sort_stats('tottime').print_stats(15)

