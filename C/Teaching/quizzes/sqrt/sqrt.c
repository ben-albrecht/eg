#include <stdio.h>
#include <math.h>

int main() {

    int NumMax;
    printf("Enter NumMax\n");
    scanf("%d", &NumMax);
    for (int i = 0; i < NumMax; i += 1) printf("%lf\n", sqrt(i));

    return 0;

}
