#!/usr/bin/env python3

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
        a = t.pencolor()[0] + 600/branchLen
        b = t.pencolor()[1] - 700/branchLen
        c = t.pencolor()[2]
        newcolor = a,b,c

        # Random angle
        Right = random.randint(20, 40)
        Left = 2*Right

        # Random Branch Length

        try:
            t.pencolor(newcolor)
        except:
            print newcolor

        t.forward(branchLen)
        t.right(Right)
        tree(branchLen-15,t, newcolor)
        t.left(Left)
        tree(branchLen-15,t, newcolor)
        t.right(Right)

        t.pencolor(color)
        t.backward(branchLen)
        t.pencolor(newcolor)
    else:
        print color

def main():

    # Initialize turtle & screen
    t = turtle.Turtle()
    myWin = turtle.Screen()

    # Brush Speed
    t.speed(5)

    # Initial Position (?)
    t.left(90)
    t.up()
    t.backward(100)
    t.down()

    # Set colormode to (1-255) rgb (instead of 0-1)
    turtle.colormode(255)

    # Intial Color (Bright Green)
    original_color = (1, 200, 40)
    t.pencolor(original_color)

    # Start recursive function
    tree(75,t, original_color)

    # Quit screen on click
    myWin.exitonclick()

main()

