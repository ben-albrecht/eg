#!/usr/bin/env python3
# encoding: utf-8

from cffi import FFI

def main():
    """ Sample code to call C library from Python to print "Hello World"
    :returns: TODO

    """

    # Instantiate FFI object
    ffi = FFI()

    # Declare function signature in C
    ffi.cdef("""
                int printf(const char *format, ...);
             """)

    # Load entire C namespace
    C = ffi.dlopen(None)

    # Equivalent to `char arg[] = "world"` in C
    arg = ffi.new("char[]", b"world")

    # Call printf with our argument
    C.printf(b"Hello, %s!\n", arg)

    return


if __name__ == '__main__':
    main()

