#include <math.h>
#include <stdio.h>
#include "copy.h"

void copy(float *in, float *out, int len) {
    int i;
    // For fun:
    printf("%f", sin(0.5));
    // Actual purpose:
    for (i = 0; i < len; i++) {
        out[i] = in[i];
    }
};
