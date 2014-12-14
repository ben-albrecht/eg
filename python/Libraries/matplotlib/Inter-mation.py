import pylab as pyl
import matplotlib.pyplot as plt
import matplotlib.widgets as wig
#from matplotlib.widgets import Slider, Button, RadioButtons

## Sin Wave Plot ##

fig = plt.figure()
ax = plt.axes(xlim=(0, 1), ylim=(-10, 10))
l, = ax.plot([], [], lw=2, color='red')

fig.add_subplot(111)
fig.subplots_adjust(left=0.25, bottom=0.25)

#t = arange(0.0, 1.0, 0.001)
## Amplitude of sin wave
a0 = 5
## Phase of sin wave
f0 = 3
## Sin wave equation applied to entire range, t
##s = a0*sin(2*pi*f0*t)
## `l,` is a plot of t vs s, with adjusted line width and color
## Save this plot as l, for later use
##l, = plot(t,s, lw=2, color='red')
#l, = plot([], [], lw=2, color='red')
#
### Slider Plot ##
## Define dimensions of a new plot
#axis([0, 1, -10, 10])


# We need to somehow put these on a subplot of some sort
# New axis color
axcolor = 'lightgoldenrodyellow'
# Define positions of sliders
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
axamp  = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

# Define Sliders, ranges, and initial values
sfreq = wig.Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
samp =  wig.Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    #l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    # draw()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = wig.Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = wig.RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    plt.draw()
radio.on_clicked(colorfunc)

def init():
    l.set_data([], [])
    return l,

import numpy as np

def animate(i):
    amp = samp.val
    freq = sfreq.val
    x = np.linspace(0, 2, 1000)
    y = amp * np.sin(2 * np.pi * (x - freq * i))
    #y = a0 * np.sin(2 * np.pi *( x - f0 * i))
    l.set_data(x, y)
    return l,

from matplotlib import animation

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=200,
                               blit=True)


plt.show()
