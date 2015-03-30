#include <math.h>
#include <stdio.h>
#include <stdlib.h>

#define _USE_MATH_DEFINES
double pi = M_PI;

double next_term(double t, int i){
    return (12.0 / pow(pi, 2)) * pow(1.0 / (2*i - 1),2) * cos((2*i - 1)*pi*t / 3.0);
}

double voltage(double t, int n) {
    /* Prints and returns the fourier analysis of a complex voltage */

    double sum = 0;
    for (int i = 1; i <= n; i += 1) {
        sum += next_term(t, i);
    }
    double V = 3/2.0 -  sum;
    printf("V(t=%.2lf, n=%d) = %lf\n\n", t, n, V);
    return V;
}


double voltage_converged(double t, double epsilon) {
    /* This function takes a time, t and convergence threshold epsilon and
     * continues to add terms until the absolute value of the next term is less
     * than or equal to epsilon */

    double sum = 0;
    int i = 1;
    while (true) {
        if ( fabs(next_term(t, i)) <= epsilon ) break;
        sum += next_term(t, i);
        i += 1;
    }

    double V = 3/2.0 - sum;
    printf("Veps(t=%.2lf, epsilon=%.4lf) = %lf\n\n", t, epsilon, V);
    return V;
}

double voltage_diff(double t1, double t2, int n) {
    /* Compute difference of voltages at t1 and t2 */

    double V = voltage(t2, n) - voltage(t1, n);
    printf("Vdiff(t1=%.2lf, t2=%.2lf, n=%d) = %lf\n\n", t1, t2, n, V);
    return V;
}

int main(void) {

    double t;
    double t1;
    double t2;
    int n;
    double epsilon;
    char response;

    // Part 1
    printf("\nPart 1: V(t, n)\n\n");
    while (true) {
        printf("Enter time, t:\n");
        scanf("%lf", &t);

        printf("Enter number of cycles, n:\n");
        scanf("%d", &n);

        voltage(t, n);

        printf("Again? [Y/n]\n");
        // White space before conversion specifier, %c
        // to absorb previous whitespace/newlines
        scanf(" %c", &response);

        if ( response != 'Y' ) break;
    }

    // Part 2
    printf("\nPart 2: Veps(t, epsilon)\n\n");
    while (true) {
        printf("Enter time, t:\n");
        scanf("%lf", &t);

        printf("Enter convergence threshold, epsilon:\n");
        scanf("%lf", &epsilon);

        voltage_converged(t, epsilon);

        printf("Again? [Y/n]\n");
        scanf(" %c", &response);

        if ( response != 'Y' ) break;
    }

    // Part 3
    printf("\nPart 3: Vdiff(t1, t2, n)\n\n");
    while (true) {
        printf("Enter time, t1:\n");
        scanf("%lf", &t1);

        printf("Enter time, t2:\n");
        scanf("%lf", &t2);

        printf("Enter number of cycles, n:\n");
        scanf("%d", &n);

        voltage_diff(t1, t2, n);

        printf("Again? [Y/n]\n");
        scanf(" %c", &response);

        if ( response != 'Y' ) break;
    }

    return 0;
}
