#!/bin/awk

BEGIN 
{
    # Before script runs.. declare some variables, etc.
    FS=" "
}

# Code to be performed on every line
{

    # Concept of fields:
    print $1, $2, $3
    # if a line were:
    #   "Hello group, how are you?"
    # This would print, 
    #   "Hello group, how" 

    print $0
    # This would print the entire line

    print $NF
    # This would print the final field

    print $NR
    # This would print the line number

    FS=","
    # This changes the field separator to a comma
    print $1
    # This would print 
    #   "Hello group" 

    # awk also supports printf (formatted print, also known as fancy print)
    printf("%30s %20.10f\n",$1, 627.50947*($3 - $2))

    FS=" "
    # This changes the field separator back to space

}

END
{
    # After script runs.. post-processing, etc.
}

