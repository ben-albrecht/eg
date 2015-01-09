# Demonstration of calling a C function from within Python 3
# This demo parses a number from char* to integer using atoi() function of stdlib.h

from libc.stdlib cimport atoi

cdef parse_charptr_to_py_int(char* s):
    """Wrapper function for atoi

    :char* s: TODO
    :returns: TODO

    """
    assert s is not NULL
    return atoi(s)

