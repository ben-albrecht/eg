#include <stdio.h>
#include <string.h>

int basic()
{
   const char src[50] = "http://www.tutorialspoint.com";
   char dest[50];

   printf("Before memcpy dest = %s\n", dest);
   memcpy(dest, src, strlen(src)+1);
   printf("After memcpy dest = %s\n", dest);

   return(0);
}


int reference()
{
    reference();
    const char * bar = "hello";   // Constant pointer to character
    const char baz[256] = "world";
    char foo[256] = "";                 // Array with allocation for 256 chars

    memcpy(&foo[0], baz, strlen(baz));

    printf("%s\n", foo);
    printf("%s\n", bar);
    printf("%s\n", baz);

    return(0);
}

int convert()
{
    const char * CHPL_COMM = "none";
    const char * arg = "gasnet";

    printf("CHPL_COMM=%s, arg=%s\n", CHPL_COMM, arg);

    CHPL_COMM = arg;

    printf("CHPL_COMM=%s, arg=%s\n", CHPL_COMM, arg);

    return(0);
}

int main() {
    //basic();
    //reference();
    convert();
}

