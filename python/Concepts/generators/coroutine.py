#!/usr/bin/env python3

def spam():
    while True:
        item = yield
        print("Got:", item)


def spam2way():
    while True:
        item = yield
        # work on item until ..
        yield item


# Usage:
# from coroutines import spam
# s = spam()
# next(s)
# s.send(anything)
# s.send(anything)
# s.send(anything)
# s.send(anything)
