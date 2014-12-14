#!/bin/sh


# Variable assignment

this="whatever"
that=10
#  ^^^ Note the whitespace
#      this = "this" will NOT work

echo "$this is a variable"
echo '$this is a variable'
echo "${this}IS a variable too"


# Conditions

if [ $this == "this" ]; then
    echo "$this is a string that matches \"this\""
elif [ $this -eq "1" ]; then
    echo "$this is a float that matches 1"
else
    return
    # exit will also work, but generally return is preferred
    #   in case you run the script in shell:
    #   > . ./basic
    #   vs.
    #   > ./basic
fi

## Conditional Statements
## If
#[ -a FILE ] # True if FILE exists.
#[ -b FILE ] # True if FILE exists and is a block-special file.
#[ -c FILE ] # True if FILE exists and is a character-special file.
#[ -d FILE ] # True if FILE exists and is a directory.
#[ -e FILE ] # True if FILE exists.
#[ -f FILE ] # True if FILE exists and is a regular file.
#[ -g FILE ] # True if FILE exists and its SGID bit is set.
#[ -h FILE ] # True if FILE exists and is a symbolic link.
#[ -k FILE ] # True if FILE exists and its sticky bit is set.
#[ -p FILE ] # True if FILE exists and is a named pipe (FIFO).
#[ -r FILE ] # True if FILE exists and is readable.
#[ -s FILE ] # True if FILE exists and has a size greater than zero.
#[ -t FD ]   # True if file descriptor FD is open and refers to a terminal.
#[ -u FILE ] # True if FILE exists and its SUID (set user ID) bit is set.
#[ -w FILE ] # True if FILE exists and is writable.
#[ -x FILE ] # True if FILE exists and is executable.
#[ -O FILE ] # True if FILE exists and is owned by the effective user ID.
#[ -G FILE ] # True if FILE exists and is owned by the effective group ID.
#[ -L FILE ] # True if FILE exists and is a symbolic link.
#[ -N FILE ] # True if FILE exists and has been modified since it was last read.
#[ -S FILE ] # True if FILE exists and is a socket.
#[ FILE1 -nt FILE2 ] # True if FILE1 has been changed more recently than FILE2, or if FILE1 exists and FILE2 does not.
#[ FILE1 -ot FILE2 ] # True if FILE1 is older than FILE2, or is FILE2 exists and FILE1 does not.
#[ FILE1 -ef FILE2 ] # True if FILE1 and FILE2 refer to the same device and inode numbers.
#[ -o OPTIONNAME ]   # True if shell option "OPTIONNAME" is enabled.
#[ -z STRING ]   # True if the length of "STRING" is zero.
#[ -n STRING ] or [ STRING ] # True if the length of "STRING" is non-zero.
#[ STRING1 == STRING2 ]  # True if the strings are equal. "=" may be used instead of "==" for strict POSIX compliance.
#[ STRING1 != STRING2 ]  # True if the strings are not equal.
#[ STRING1 < STRING2 ]   # True if "STRING1" sorts before "STRING2" lexicographically in the current locale.
#[ STRING1 > STRING2 ]   # True if "STRING1" sorts after "STRING2" lexicographically in the current locale.
#[ ARG1 OP ARG2 ]        # "OP" is one of -eq, -ne, -lt, -le, -gt or -ge. 
## These arithmetic binary operators return true if "ARG1" is equal to,
## not equal to, less than, less than or equal to, greater than,
## or greater than or equal to "ARG2", respectively. "ARG1" and "ARG2" are integers.
#
## Combination / Modifiers:
#[ ! EXPR ]          # True if EXPR is false.
#[ ( EXPR ) ]        # Returns the value of EXPR. This may be used to override the normal precedence of operators.
#[ EXPR1 -a EXPR2 ]  # True if both EXPR1 and EXPR2 are true.
#[ EXPR1 -o EXPR2 ]  # True if either EXPR1 or EXPR2 is true.


# Iteration

# For loop

for i in $( ls ); do
    echo item: $i
done

for i in `ls`; do
    echo item: $i
done

for i in `seq 1 10`; do
    echo $i
done 


# While loop
COUNTER=0
while [  $COUNTER -lt 10 ]; do
    echo The counter is $COUNTER
    let COUNTER=COUNTER+1 
done

while read p; do
    echo $p
done <sample.txt

# Until loop

COUNTER=20
until [  $COUNTER -lt 10 ]; do
    echo COUNTER $COUNTER
    let COUNTER-=1
done


# Functions

basic_function () {
    echo "This function does nothing, but echos argument 1 : $1"
    return
}




