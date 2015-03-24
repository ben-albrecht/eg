#!/usr/bin/env python3

from cffi import FFI

def main():

    ffi = FFI()
    ffi.cdef(""" void ReadWrapper(char const * filename); """)
    ffi.dlopen("libread.so")


if __name__ == '__main__':
    main()
