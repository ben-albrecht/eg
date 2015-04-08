#include <stdio.h>   // printf(), scanf()
#include <math.h>    // pow(), pi
#include <stdbool.h> // bool
#include "hw14.h"    // custom functions

#define _USE_MATH_DEFINES
double pi = M_PI;

int main(void) {

    printout();

    bool dobreak = false;
    char response;
    double r = 0;

    for (;!dobreak;) {
        response = 'a';
        int dimensions = promptdimensions();
        switch (dimensions) {
            case 2:
                // Get parameters
                while( r <= 0.0 ) {
                    printf("Please give a length: ");
                    scanf("%lf", &r);
                }
                circle(r);
                square(r);
                break;

            case 3:
                // Get parameters
                while( r <= 0.0 ) {
                    printf("Please give a length: ");
                    scanf("%lf", &r);
                }
                sphere(r);
                cube(r);
                break;

            default:
                break;
        }


        for(;;) {
            printf("Do you want to do this again? (y/n)\n");
            scanf(" %c", &response);
            if (response == 'y' ||  response == 'Y') {
                printf("Restarting\n");
                break;
            }
            else if (response == 'N' || response == 'n') {
                printf("Quitting\n");
                dobreak = true;
                break;
            }
            else {
                printf("That is not an acceptable response\n");
            }
        }
    }

    return 0;
}


void printout() {
    // Function 1 : Print program's purpose
    printf("This program will find the area and perimeter of a two dimensional\n\
        shape, or the volume and surface area of a three dimensional shape\n");
}


int promptdimensions() {
    // Function 2 : Get dimensions from user
    int dimensions = 0;
    while (dimensions != 2  && dimensions != 3) {
        printf("How many dimensions for shape? [2] or [3]\n\n");
        scanf(" %d", &dimensions);
    }
    return dimensions;
}


void circle(double r) {
    // Function 4: Computes 2D properties of circle
    double area = pi*pow(r, 2);
    double perimeter= 2*pi*r;
    printf("Circle of Radius: %f\n", r);
    printf("Area:             %f\n", area);
    printf("Circumference:    %f\n", perimeter);
}

void square(double r) {
    // Function 4: Computes 2D properties of square
    double area = pow(r, 2);
    double perimeter= 4*r;
    printf("Square of Length: %f\n", r);
    printf("Area:             %f\n", area);
    printf("Perimeter:        %f\n", perimeter);
}

void sphere(double r) {
    // Function 4: Computes 2D properties of square
    double volume = (4.0/3.0) * pi * pow(r, 3);
    double perimeter= 4*pi*pow(r, 2);
    printf("Sphere of Radius: %f\n", r);
    printf("Volume:           %f\n", volume);
    printf("Surface Area:     %f\n", perimeter);
}

void cube(double r) {
    // Function 4: Computes 2D properties of square
    double volume = pow(r, 3);
    double perimeter = 6*pow(r, 2);
    printf("Cube of Length:   %f\n", r);
    printf("Volume:           %f\n", volume);
    printf("Surface Area:     %f\n", perimeter);
}
