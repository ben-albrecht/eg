#!/usr/bin/env python3


def spam(n):
    """Any function with "yield" is a generator"""
    yield n


def spamexit():
    """ TODO Can specify what happens when g.close() called
        Not really sure how this works yet... """
    num = 0
    try:
        while True:
            try:
                num = (yield num)
            except GeneratorExit:
                # Caught by g.close()
                # Code here is for internal function cleanup
                print("except generatorexit")
            num += 1
    finally:
        # Reached after g.close()
        # Code here is communicated back to user
        print("Generator successfully closed!")
        return 0


def spamexcept():
    """ Yielding Exceptions
        val = g.throw(RuntimeError, 'Broken') will yield 
        return statement in RuntimeError """
    num = 0
    while True:
        try:
            yield num
        except RuntimeError as e:
            return 1
            # This can be done via eggs.close() from cml


def spamreturn():
    """ What happens if you have return after generator yield? """
    yield 42
    # Calling next() a second time will result in
    #   StopIteration error with "eggs" as return
    return "eggs"



