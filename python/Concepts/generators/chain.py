#!/usr/bin/env python3

def chain(x, y):
    """ Stacking Generators:
        Exhausts yields from x, then exhausts yields from y """
    # "yield from" is known as "delegation"
    yield from x
    yield from y



if __name__ == "__main__":
    a = [1,2,3]
    b = [4,5,6]

    for n in chain(a,b):
        print(n)


    # Nested chains, aka chaining chains
    for n in chain(chain(a,b),chain(b,b)):
        print(n)
