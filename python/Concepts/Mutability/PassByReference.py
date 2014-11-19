#!/bin/env python
"""
Demonstration of mutable vs. immutable objects in python
and how passing by reference works differently than in, say C++
"""

class PassByReference:
    def __init__(self, List = [1, 2, 3, 4], Tuple = (1, 2, 3, 4)):
        """
        Intrinsic Immutables
        ====================
        Numbers
        Sequences: Strings, Unicode, Tuples
        Types: Frozen Sets `frozenset()`
        Mappings: (none)
        """

        # Some Examples
        self.String = "Hello World" # Strings are immutable
        self.Number = 42            # Numbers are immutable
        self.Tuple  = Tuple  # Tuples are immutable

        """
        Intrinsic Mutables
        ==================
        Sequences: Lists, Byte Arrays, (non-instrinsic: module array)
        Types: Sets `set()`
        Mappings: Dictionaries `{..}`
        """

        # Some Examples
        self.List   = List           # Lists are mutable
        self.Dist   = {'a':1, 'b':2} # Dicts are mutable


    def change_list(self, the_list):
        print '\ngot', the_list
        the_list.append(5)
        print 'changed to', the_list


    def change_tuple(self, the_tuple):
        print '\ngot', the_tuple
        the_tuple += (4,)
        print 'changed to', the_tuple

if __name__ == "__main__":
    outer_list = ['a', 'b', 'c']
    outer_tuple = ('a', 'b', 'c')

    # Instantiate PassByReference object
    pbr = PassByReference(List = outer_list, Tuple = outer_tuple)
    print "\npbr.list", pbr.List
    print "outer_list", outer_list

    # Change list inside of pbr - affects list inside and outside of pbr
    pbr.change_list(pbr.List)
    print "\npbr.list", pbr.List
    print "outer_list", outer_list

    # Change list outside of pbr - affects list inside and outside of pbr
    outer_list.append('e')
    print "\npbr.list", pbr.List
    print "outer_list", outer_list

    # Change value of list element outside of pbr - affects both still
    outer_list[3] = 'd'
    print "\npbr.list", pbr.List
    print "outer_list", outer_list


    # Check Tuples
    print "\npbr.tuple", pbr.Tuple
    print "outer_tuple", outer_tuple

    # Change tuple inside of pbr in method - Won't affect either,
    # because a copy of pbr.Tuple is made within the class method
    pbr.change_tuple(pbr.Tuple)
    print "\npbr.tuple", pbr.Tuple
    print "outer_tuple", outer_tuple

    # Change tuple outside of pbr -
    # outer_tuple is reassigned to a new tuple entirely,
    # while pbr still has the original reference
    outer_tuple += ('e',)
    print "\npbr.Tuple", pbr.Tuple
    print "outer_tuple", outer_tuple

    # We cannot re-assign any values of a tuple,
    # we must call a function to redefine the tuple entirely (and lose its original reference)
