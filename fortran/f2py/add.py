#!/usr/bin/env python3

import addprocedures

def main():
    result = addprocedures.addfunction(10, 20)
    print("addfunction(10, 20) = ", result)

    # If using intent (in) / intent (out),
    # f2py turns subroutines into functions that return (out)
    result = 0.0
    result = addprocedures.addroutine(20, 20)
    print("addsubroutine(20, 20, result)\nresult = ", result)


if __name__ == '__main__':
    main()
