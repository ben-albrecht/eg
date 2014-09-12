#!/bin/bash


# This script is an example of cases
# Note: If multiple definitions exist, the case that first matches the variable ($space) will occur

echo "enter value for \$space , [1-99]"
read space


case $space in
[1-6]*) # 1-69
  Message="All is quiet."
  ;;
[7-8]*) # 70-89
  Message="Start thinking about cleaning out some stuff.  There's a partition that is $space % full."
  ;;
9[1-8])	# 91-98
  Message="Better hurry with that new disk...  One partition is $space % full."
  ;;
99)     # 99
  Message="I'm drowning here!  There's a partition at $space %!"
  ;;
*)	# anything else
  Message="I seem to be running with an nonexistent amount of disk space..."
  ;;
esac

echo $Message 

