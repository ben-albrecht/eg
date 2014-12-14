#!/usr/bin/env python

def move(n, frompole, topole, withpole):
    if n == 1:
        print frompole, " to ", topole
    else:
        move(n - 1, frompole, withpole, topole)
        print frompole, " to ", topole
        move(n - 1, withpole, topole, frompole)

# Number of blocks:
n = 5
move(5, 'A', 'B', 'C')
