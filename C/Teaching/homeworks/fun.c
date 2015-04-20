#include <stdlib.h> // malloc()
#include <stdio.h>  // printf()

typedef struct {
    int x;
    int y;
    int z;
} vector;


void squared(int mat[4][4]) {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            mat[i][j] =  mat[i][j] * mat[i][j];
        }
    }
}

void squaredvec(int *vec, int N) {
    for (int i = 0; i < N; i++) {
        vec[i] =  vec[i] * vec[i];
    }
}

int main() {

    vector V;

    V.x = 1;
    V.y = 2;
    V.z = 3;

    //arrays:
    int arr[4];
    int *arr1 = (int *)malloc(4*sizeof(int));


    int mat[4][4];
    squared(mat);

    int vec[4];
    squaredvec(vec, 4);

    //int **mat = matrixgen();


    /*
    double *C = (double *)malloc(sizeof(double));
    // static_cast<double *>

    *C = 10.1234;


    printf("%lf\n", *C);

    free(C);
    */

}
