#!/usr/bin/env python3
# encoding: utf-8

from cffi import FFI
import argparse

def get_arguments(args=None):
    """
    Get arguments from command line
    :args: Arguments, if predefined
    :returns: Opts, the arguments parsed
    """
    parser = argparse.ArgumentParser(prog = 'main.py',
                                     usage = '%(prog)s inputfile [options] ',
                                     description = ''' %(prog)s is a test to pass ifstream data types to C via cffi''',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter
                                     )
    parser.add_argument('finp', help='input file')
    opts = parser.parse_args(args)
    return opts


def main(opts):
    """ Take an inputfile, create an ifstream and pass it to C program  """

    ffi = FFI()
    ffi.cdef('''extern C {
                    void progman(std::ifstream &finp);
                }''')
    C = ffi.dlopen('libprogman.so')
    finp = opts.finp
    #Cfinp = ffi.cast("float *", b.ctypes.data)
    #C.progman(Cfinp)

    return


if __name__ == '__main__':
    opts = get_arguments()
    main(opts)
