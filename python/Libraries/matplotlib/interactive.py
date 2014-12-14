from pylab import *
from matplotlib.widgets import Slider, Button, RadioButtons

## Sin Wave Plot ##

# Create sub-plot of dimensions 1x1, labeled subplot 1
ax = subplot(111)
# Adjust sub-plot 0.25 to the left, and 0.25 down (units)?
subplots_adjust(left=0.25, bottom=0.25)
# `t` is range 0 to 1.0, in 0.001 increments
t = arange(0.0, 1.0, 0.001)
# Amplitude of sin wave
a0 = 5
# Phase of sin wave
f0 = 3
# Sin wave equation applied to entire range, t
s = a0*sin(2*pi*f0*t)
# `l,` is a plot of t vs s, with adjusted line width and color
# Save this plot as l, for later use
l, = plot(t,s, lw=2, color='red')

## Slider Plot ##
# Define dimensions of a new plot
axis([0, 1, -10, 10])

# New axis color
axcolor = 'lightgoldenrodyellow'
# Define positions of sliders
axfreq = axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
axamp  = axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)

# Define Sliders, ranges, and initial values
sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*sin(2*pi*freq*t))
    draw()
sfreq.on_changed(update)
samp.on_changed(update)

resetax = axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = axes([0.025, 0.5, 0.15, 0.15], axisbg=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    draw()
radio.on_clicked(colorfunc)

show()
