#!/usr/bin/env python3

from cffi import FFI

def main():
    ffi = FFI()
    ffi.cdef(""" void ReadWrapper(char const * filename);""")
    C =ffi.dlopen("./libread.so")
    C.ReadWrapper(b"file.txt")


if __name__ == "__main__":
    main()
