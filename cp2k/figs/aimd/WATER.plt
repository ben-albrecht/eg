#!/usr/local/bin/gnuplot -persist

plot 'WATER-1.ener' u 2:6 w l
replot 'WATER-1.ener' u 2:5 w l
