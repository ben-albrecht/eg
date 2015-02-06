
//
// main.c
//

#include "read.h"
#include <stdio.h>

int main() {

    FILE *f = fopen("file.txt", "w");
    const char *text = "foo bar baz";
    fprintf(f,"%s", text);
    fclose(f);

    const char *filename = "file.txt";
    ReadWrapper(filename);

    return 0;
}
