#!/usr/bin/gnuplot -persist

#set terminal x11   # terminal type: for a Mac, use "aqua" instead of "x11"
# AXIS
set xlabel 'x title'
set ylabel 'y title'
set xrange [0:5]    # x-range
set yrange [0:1]    # y-range
#set xtics 0.01      # Minor Ticks
#set mxtics 4        # Major Ticks
#set ytics 0.0001    # Minor Ticks
#set mytics 4        # Major Ticks

#f(x) = m*x + b
#fit f(x) "a.dat" 1:2 via m, b
stats "a.dat" u 1:2
set grid                    # Turn on grid lines
set pointsize 2.0           # set the size of the plotted points
set key bottom right        # also top left
#set timestamp              # turn on a date/time indicator
plot "a.dat" using 1:2 pt 7 t ""
set out "example.ps"        # name of the output postscript file
set terminal postscript         # switch to postscript mode
replot
