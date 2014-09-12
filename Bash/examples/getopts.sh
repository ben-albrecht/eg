#!/bin/sh


while getopts "1234" OPTION		# Possible Options -1 , -2, -3, -4
do
   case $OPTION in
	1)  echo "one"
            echo "one";;		# ";;" ends the option
	2)  echo "two";;
	3)  echo "three";;
        4)  echo "four";;

	\?) exit 1;;			# error msg given
   esac
done
