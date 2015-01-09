#!/usr/bin/env python

"""
My attempt at the Tower of Hanoi Problem

Base Case:
    Move 1 rung from
"""

def move(numpole, frompole, topole, bystander):
    if numpole < 1:
        return
    move(numpole - 1, frompole, bystander, topole)
    MoveOutput(frompole, topole)
    move(numpole - 1, topole, bystander, frompole)



def MoveOutput(frompole, topole):
    print "Move ", frompole, " to ", topole



if __name__ == '__main__':
    move(3, 'A', 'B', 'C')
