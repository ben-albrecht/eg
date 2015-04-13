// Function takes an array and returns an array

#include <stdio.h> // printf()

#define dim 4

int *squared(int *array) {
    // Function returns an array: for variable dim with static array,
    //   must define dim in preprocessor diretive
    static int newarray[dim];
    for (int i=0; i<dim; i++) {
        newarray[i] = array[i] * array[i];
        array[i] = array[i] * array[i];
    }
    return newarray;
}

void squaredref(int *array, int dim) {
    // pass by reference instead of returning matrix
    for (int i=0; i<dim; i++) {
        array[i] = array[i] * array[i];
    }
}


void matrixadd(int *AB, int *A, int *B, int N, int M) {
    // Add 2 matrices element-wise
    // AB needs to be allocated before passed
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            AB[i][j] = A[i][j] + B[i][j];
        }
    }
}

void squaredint(int* var) {
    *var = *var * *var;
}

int main() {

    printf("Hello World\n");
    int array[dim];

    for (int i=0; i<dim; i++) {
        array[i] = i*10;
        printf("array[%d] = %d\n", i, array[i]);
    }

    int *newarray = squared(array);

    printf("int *newarray = squared(array);\n");
    for (int i=0; i<dim; i++) {
        printf("newarray[%d] = %d\n", i, newarray[i]);
    }

    for (int i=0; i<dim; i++) {
        printf("array[%d] = %d\n", i, array[i]);
    }

    int var = 5;
    printf("var = %d\n", var);
    squaredint(&var);
    printf("squaredint(&var)\n");
    printf("var = %d\n", var);


    /*
    int *A;
    int *B;
    int *AB;
    int rows = 5;
    int cols = 5;

    // This will change AB to A + B
    matrixadd(AB, A, B, rows, cols);
    */




    return 0;
}
