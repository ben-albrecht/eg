#include <stdio.h>
#include "matrixmult.h"
#include <mpi.h>

void matrixproduct(double A, double B, double C) {
    // C = A * B

}

//void test(double );
void test(double A[][]) {

}

int main() {
    return 0;
    int N = 2;
    double A [N][N];
    double B [N][N];
    double C [N][N];
    //matrixproduct(A, B, C);
    test(A)
}

/*
 * Initialize MPI Execution Environment 
int MPI_Init(int *argc, char ***argv);
int MPI_Abort(MPI_Comm comm, int errorcode)
*/




