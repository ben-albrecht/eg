#!/usr/bin/env python

import turtle
import random
"""
Modify the thickness of the branches so that as the branchLen gets smaller, the line gets thinner.
Modify the color of the branches so that as the branchLen gets very short it is colored like a leaf.
Modify the angle used in turning the turtle so that at each branch point the angle is selected at random in some range. For example choose the angle between 15 and 45 degrees. Play around to see what looks good.
Modify the branchLen recursively so that instead of always subtracting the same amount you subtract a random amount in some range.
Run
"""


def tree(branchLen, t, color):
    t.pensize(branchLen/12)

    if branchLen > 5:
        # Slowly change initial color
        a = t.pencolor()[0] #+ 600/branchLen
        b = t.pencolor()[1] #- 700/branchLen
        c = t.pencolor()[2]
        newcolor = a,b,c

        # Random angle
        Right = random.randint(20, 40)
        Left = 2*Right

        # Random Branch Length
        dLen = random.randint(15,15)

        try:
            t.pencolor(newcolor)
        except:
            print newcolor

        t.forward(branchLen)
        t.right(Right)
        tree(branchLen-dLen, t, newcolor)
        t.left(Left)
        tree(branchLen-dLen, t, newcolor)
        t.right(Right)

        t.pencolor(color)
        t.backward(branchLen)
        t.pencolor(newcolor)
    else:
        print color


def f(screen):
    print "quit!"
    screen.bye()
    exit(1)


def main():

    # Initialize turtle & screen
    t = turtle.Turtle()
    myWin = turtle.Screen()
    #myWin.screensize(1000,1000)

    # Want to make spacebar quit the program
    #myWin.onkey(f, " ")
    #myWin.listen()

    # Brush Speed
    t.speed(5)

    # Initial Position (?)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Set colormode to (1-255) rgb (instead of 0-1)
    #turtle.colormode(255)

    # Intial Color (Bright Green)
    original_color = (0.1, 1.0, 0.1)
    t.pencolor(original_color)

    # Start recursive function
    tree(75,t, original_color)

    # Quit screen on click
    myWin.exitonclick()

main()

