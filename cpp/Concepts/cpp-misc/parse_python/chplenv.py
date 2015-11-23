#!/usr/bin/env python

from __future__ import print_function

if __name__ == '__main__':
    print("""CHPL_HOST_PLATFORM=darwin
CHPL_HOST_COMPILER=clang
CHPL_TARGET_PLATFORM=darwin
CHPL_TARGET_COMPILER=clang
CHPL_TARGET_ARCH=native
CHPL_LOCALE_MODEL=flat
CHPL_COMM=none
CHPL_COMM_SUBSTRATE=none
CHPL_GASNET_SEGMENT=none
CHPL_TASKS=qthreads
CHPL_THREADS=none
CHPL_LAUNCHER=none
CHPL_TIMERS=generic
CHPL_MEM=cstdlib
CHPL_MAKE=make
CHPL_ATOMICS=intrinsics
CHPL_NETWORK_ATOMICS=none
CHPL_GMP=none
CHPL_HWLOC=hwloc
CHPL_REGEXP=none
CHPL_WIDE_POINTERS=struct
CHPL_LLVM=none
CHPL_AUX_FILESYS=none""")
