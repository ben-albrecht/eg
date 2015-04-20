#include <stdio.h>
#include <stdlib.h>

#define N 3

void addmat(int, double[][N], double [][N], double[N][N]);

int main() {
    int dim = 3;
    int A[][N] = {1,2,3,4,5,6,7,8,9}; // Matrix A
    int B[][N] = {9,8,7,6,5,4,3,2,1}; // Matrix B
    int C[N][N];

    addmat(dim, A, B, C);

    for (int i = 0; i < dim; i ++) {
        for (int j = 0; j < N; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }
    return 0;
}



void addmat(int dim, double A[][N], double B[][N], double C[N][N]) {
    for (int i = 0; i < dim; i ++) {
        for (int j = 0; j < N; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}

