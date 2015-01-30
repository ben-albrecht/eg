#include <math.h>
#include <stdio.h>

void copy(float *in, float *out, int len) {
    // For fun:
    printf("%f", sin(0.5));
    // Actual purpose:
    for (int i = 0; i < len; i++) {
        out[i] = in[i];
    }
};
