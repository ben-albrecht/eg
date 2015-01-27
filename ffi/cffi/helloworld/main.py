#!/usr/bin/env python3
# encoding: utf-8

from cffi import FFI
import numpy as np

def main():
    """call foo library
    :returns: TODO

    """
    ffi = FFI()
    ffi.cdef("extern void foo(void);")
    C = ffi.dlopen("libfoo.so")
    C.foo()
    return


if __name__ == '__main__':
    main()
