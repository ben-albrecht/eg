#include <stdio.h>
#include <ctype.h>
#include <math.h>

int main() {

    char filename[80];
    FILE *infile;
    for (;;) {
        printf("What file would you like to read in?\n");
        scanf("%s", filename);
        if ((infile = fopen(filename, "r"))) break;
        else printf("%s does not exist\n", filename);
    }

    // Count the number of values in the file:
    double value;
    int numbers = 0;
    for (;;) {
        if (fscanf(infile, "%lf", &value) == EOF) break;
        else numbers += 1;
    }
    fclose(infile);

    printf("numbers: %d\n", numbers);

    // Reopen file
    infile = fopen(filename, "r");
    double arr[numbers];
    for(int i = 0; i < numbers; i++) {
        fscanf(infile, "%lf", &arr[i]);
    }
    fclose(infile);

    char response;
    for (;;) {
        printf("What would you like to print?\n");
        printf("[N]umbers\n");
        printf("[L]og of the numbers");
        scanf(" %c", &response);
        if (toupper(response) == 'N' || toupper(response) == 'L') break;
        else printf("Please enter 'N' or 'L'\n");
    }



    if (response == 'N') for(int i = 0; i < numbers; i++) printf("%lf\n", arr[i]);
    else for(int i = 0; i < numbers; i++) printf("%lf\n", log(arr[i]));

    return 0;
}
