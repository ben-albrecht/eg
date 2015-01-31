#!/usr/bin/env python3
# encoding: utf-8

from cffi import FFI
import numpy as np

def main():
    """ Pass a numpy array to a C function and get a numpy array back out
        Cleaned up version, from:
        http://stackoverflow.com/questions/16276268/how-to-pass-a-numpy-array-into-a-cffi-function-and-how-to-get-one-back-out
    """

    ffi = FFI()
    ffi.cdef("void copy(float *in, float *out, int len);")
    C = ffi.dlopen("./libcopy.so")

    # Create float32 numpy array
    a = 42 * np.ones(16, dtype=np.float32)
    b = np.zeros_like(a)

    # Cast data to readable format by C
    pa = ffi.cast("float *", a.ctypes.data)
    pb = ffi.cast("float *", b.ctypes.data)

    C.copy(pa, pb, len(a))

    # pb is C version of b, so values of b still changed
    print(b)
    return


def main_old():
    """ Pass a numpy array to a C function and get a numpy array back out
    More Verbose, but valid

    """

    ffi = FFI()
    ffi.cdef("void copy(float *in, float *out, int len);")
    C = ffi.dlopen("libcopy.so")


    float_in = ffi.new("float[16]")
    float_out = ffi.new("float[16]")

    arr_in = 42 * np.ones(16, dtype=np.float32)
    float_in[0:16] = arr_in[0:16]

    C.copy(float_in, float_out, 16)

    arr_out = np.frombuffer(ffi.buffer(float_out, 16*4), dtype = np.float32)

    print(arr_out)
    return


if __name__ == '__main__':
    main()
