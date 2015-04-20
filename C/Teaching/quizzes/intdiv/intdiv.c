#include <stdio.h>

int main() {
    /*
     *   double @ double = double
     *   double @ int = double
     *   int @ int = int (rounded down)
     *
     */
    double celsius1 = 5 / 9 * (68.0 - 32);
    double celsius2 = 5 * (68.0 - 32) / 9;
    double celsius3 = (68.0 - 32) * 5.0 / 9.0;
    printf("%lf\n", celsius1);
    printf("%lf\n", celsius2);
    printf("%lf\n", celsius3);
    return 0;
}
