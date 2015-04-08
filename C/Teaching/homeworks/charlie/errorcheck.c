#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <ctype.h>

double numget(void);
/* This is a simple input/output function.
    It asks the user for a number, displays that number,
    and then asks if they want a new number instead.
    It also error checks and reasks the question if user
    enters invalid response */
double numdo(double);
/*This function multiplies num from "numdo()" by 2.
    It asks if user would like to rerun the equation.
    It reasks question if user enters a invalid response*/
int main(void){
    char doagain = 'Y';
    char F=2;
    while (doagain == 'Y'){
        double num = numget();
        double product = numdo(num);
        product;
        int check = 1;
        while (check == 1){
            printf("would you like to run again with a new number? (y or n):  ");
            scanf(" %c", &doagain);
            doagain = toupper(doagain);
            if (toupper(doagain) == 'Y' || toupper(doagain == 'N')){
                check = 2;
            }
        }
    }
    scanf("%c", &F);
}

double numget(void){
    char doagain1 = 'N';
    double num;
    while (doagain1 == 'N'){

        printf("choose any number  :");
        scanf("%lf", &num);
        printf("%lf\n\n", num);

        int doagain2 = 1;
        while (doagain2 == 1){
            printf("is this the number you want? (y or n):  ");
            scanf(" %c", &doagain1);
            /* must put space when before %c and time scanf is used.
                This is a replacement technique for fflush(stdin) */
            doagain1 = toupper(doagain1);
            if (doagain1 == 'Y' || doagain1 == 'N'){
                doagain2 = 2;
            }
        }
    }
    return num;
}

double numdo(double num){
    char doagain3 = 'Y';
    double product;
    while (doagain3 == 'Y'){
        product = 2 * num;
        printf("%lf x 2 = %lf\n\n", num, product);
        int doagain4 = 1;
        while (doagain4 == 1){
            printf("do you want to run again with the same numbers? (y or n):  ");
            scanf(" %c", &doagain3);
            doagain3 = toupper(doagain3);
            if (doagain3 == 'Y' || doagain3 == 'N'){
                doagain4 = 2;
            }
        }

    }
    return product;
}
