#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//#define <cmath.h>
//#_USE_DEFINITIONS
//double = M_PI;
double pi = 3.1415;

void circle(double R){
    double a = pi*pow(R, 2);
    double c = 2 * pi*R;
    printf("The area of your circle is %lf\n\n", a);
    printf("The circumference of your circle is %lf\n\n", c);
}

void square(double R){
    double a = R*R;
    double p = 4*R;
    printf("The area of your square is %lf\n\n", a);
    printf("The perimeter of your square is %lf\n\n", p);
}

void box(double R){
    double V = pow(R, 3);
    double SA = 6 * pow(R, 2);
    printf("The volume of your box is %lf\n\n", V);
    printf("The Surface Area of your box is %lf\n\n", SA);
}

void sphere(double r){
    double V = 4 / 3 * pi*pow(r, 3);
    double SA = 4 * pi*pow(r, 2);
    printf("The volume of your sphere is %lf\n\n", V);
    printf("The surface area of your sphere is %lf\n\n", SA);
}


void Header(){
    printf("This program will find the area and perimeter of a two dimensional shape, or the volume and surface area of a three dimensional shape.\n\n\
Nathan Wolk, Charles Frye, Sravan Rajathilak\n\nGroup: R18\n\n\n");

}

int dimension2(void){
    int dimension;
    printf("2d or 3d?(2 or 3):  ");
    scanf("%d", &dimension);
    printf("You chose %dd \n", dimension);
    return dimension;

}



//part1
int main(void) {

    Header();
    int dimension;
    dimension = dimension2();
    switch (dimension){
    case 2:{

               double R;
               printf("radius/side?");
               scanf("%lf", &R);
               circle(R);
               square(R);
               system("pause");
               break;
    }
    case 3:{
               double R;
               printf("radius/side length?\n\n");
               scanf("%lf", &R);
               sphere(R);
               box(R);
               system("pause");

    }

    }
}
