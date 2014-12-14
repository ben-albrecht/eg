import pyglet, math, Tkinter, sys


def distance(point_1=(0, 0), point_2=(0, 0)):
    """Returns the distance between two points"""
    return math.sqrt(
            (point_1[0] - point_2[0]) ** 2 +
            (point_1[1] - point_2[1]) ** 2)


def center_image(image):
    """Sets an image to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2

def get_dimensions():
    # TODO: test on Mac & Windows
    if sys.platform == 'darwin':
        # Mac
        #print NSScreen.mainScreen().frame()
        #dim  
        #NSScreen.mainScreen().frame().width
        #NSScreen.mainScreen().frame().height
        # macbookpro 13'' =1280x800 (640, 400)
        dim = [1280, 800]
    else:
        # Linux
        t = Tkinter.Tk()
        t.attributes("-alpha", 00)
        t.attributes('-fullscreen', True)
        t.update()
        dim = [t.winfo_width(), t.winfo_screenheight()]
        t.destroy()
    return dim




