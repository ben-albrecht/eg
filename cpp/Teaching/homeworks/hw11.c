#include <stdio.h>
#include <string.h>


int main()
{
    // Part 0
    printf("Charles Frye\n");
    printf("R18\n");
    printf("Bon @ 6p\n");
    printf("Nate Wolk, Sravan Rajathilak\n");
    printf("3-18-15\n\n");


    // Part 1
    printf( \
       "\nThe first \\n puts the text on a new line, the double slash by the n is \
       \nneeded to allow the printing of the \\n in this printout. If you want to add \
       \na tab in the print out you insert \\t it will tab the text as shown here. \
       \
       \n\nSometimes it is nice to print out text in \"double quotes\", this requires the \
       \ndouble quote escape sequence \\\". Sometimes it is nice to print out text in \
       \n'single quotes', this requires the single quote escape sequence \\\'.\
       \
       \n\nWant to printout a %% sign you need to use the escape sequence \"%%%%\", do you \
       \nunderstand \
       \nthe code required to print this sequence out\\\? \
       \
       \n\nFinally, notice all the single slashs '\\' at the end of each line. These \
       \nallow you to wrap the printf string to the next line for easy or reading. \
       \nMake a bell ring at this point. Did you hear the bell ring?\n" \
       );


     // Part 2
     int A = 1;
     printf("A = %i\n", A);

     // TODO: B = 2.34, C = 'f'


     // TODO: Part 3  G = [3 5 8 9]

     // TODO: Part 4 H = [4.4 5.5, 6.6 7.7]
}

