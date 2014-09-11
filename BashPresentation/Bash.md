# Group Meeting - The Powerful Tools of Bash, Awk, Sed, and Regex



                        9/12/14
                     Ben Albrecht



# Strings and Unix
“The string is a stark data structure
and everywhere it is passed there is
much duplication of process. It is a
perfect vehicle for hiding information”
    -- Alan Perlis, Computer Scientist

“Unix is an alliance of loosely
structured text files bound together and
governed by scripts. Unix is the United
Confederation of Strings”
    -- Matt Might, Some Guy on Twitter

Many of the original tools of unix are
designed for manipulating strings.

# The Toolbox
-Regular Expressions (regex)
-grep
-sed
-AWK

# The Unix Shell - Bash

History:
A Unix Shell written for the GNU Project
as a replacement for the Bourne
shell(sh) in 1989

Fun Fact: 
Bash stands for Bourne-again shell,
implying a spiritual rebirth of Bourne
shell

Usage:
Bash is a command processor typically
run in a terminal, but can also read
commands from a file, known as a script.

Like all Unix shells, bash supports:
variables ($foo) 
control structures for condition-testing (if[ ]; then .. fi)
wildcarding (\*)
piping (|) 
iteration (for, while).

#!/bin/bash

echo "Hello World!"

# AWK
History:
An interpreted programming language
created in Bell Labs in 1977.

Fun Fact:
AWK is an acronym of the last names of
its authors: Aho, Weinberger, and
Kernighan.

Usage:
AWK is designed for text processing and data
extraction. 

#!/bin/awk

BEGIN {
< Does whatever is in here at start of
script >
}

{
<Does whatever is in here to every line
of the file>
}

END {
< Does whatever is in here at end of
script >
}

# sed
History: sed (stream editor) is a Unix
utility developed in 1974 at Bell Labs, based on the
previous ed (editor), and earlier qed
(quick editor). 


Fun Fact:
sed was one of the earliest tools to
support regular expressions


Usage:
sed is designed to parse and transform
text. The most common usage of sed is
the substitution command, which replaces
an occurence of a string by another
within a given range of a given file.

# regex
History: 
Regular expressions originated in 1956
by mathematician Stephen Kleene to
describe regular languages

Fun Fact:


Usage:


# grep



# presenting.vim



# Usage


:StartPresenting
Navigation:

 * n - next slide
 * p - previous slide
 * q - quit

# The End



**Thanks!**

# After the End

Making a basic bash script (eg calling
qchem)

Setting/unsetting environment variables

For loops for automating jobs

String manipulation (eg search/replace)

If statements eg checking whether job has completed successfully

Passing command line arguments into script

Functions

Spawning threads / waiting

Algebra in bash


Grep & sed & awk:
Extract scf and mp2 energy from qchem
