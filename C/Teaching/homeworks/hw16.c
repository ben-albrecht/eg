#include <stdlib.h> // malloc(), free()
#include <stdio.h> // printf()

// These would typically go in hw16.h:

// Structs
struct matrix {
    // Struct for matrix information
    int N;
    int M;
    // Double pointer used because dimensions not yet known
    double **values;
};

// Functions
struct matrix new_matrix(int N, int M);
struct matrix read_matrix(FILE* matrixfile);
struct matrix add(struct matrix A, struct matrix B);
void print(struct matrix A, char* msg);


int main() {

    FILE* matrixfileA = fopen("matrix.dat", "r");
    struct matrix A = read_matrix(matrixfileA);
    fclose(matrixfileA);

    FILE* matrixfileB = fopen("matrix.dat", "r");
    struct matrix B = read_matrix(matrixfileB);
    fclose(matrixfileB);

    print(A, "A matrix");
    print(B, "B matrix");

    struct matrix C = add(A, B);
    print(C, "C matrix");

    // TODO:
    //   Finish functions: subtraction, multiplication, element-wise multiplication
    //   User-interface to ask what they want to do
    //   Create (A-F).dat containing all the test matrices


    return 0;

}


/*
// Recall the alternative form:

    typedef matrix {
        // Struct for matrix information
        int N;
        int M;
        double **values;
    } matrix;

// where we could instead initialize the struct with:

    matrix A;

*/

struct matrix new_matrix(int N, int M)
{
    // 'Constructor' of struct matrix, necessary because of dimension-dependence

    struct matrix A;
    A.N = N;
    A.M = M;

    // Allocate N-rows of double pointers
    A.values = malloc(N*sizeof(double *));

    // Allocate M-columns of double points for each row
    for (int i = 0; i < N; i++) A.values[i] = malloc(M*sizeof(double *));

    return A;
}

/*
Recall the alternative to the Dot operator (A.N):

    Arrow operator:
        A->N

    which is the same as (*A).N
    Note: Arrow operator can be overloaded and Dot operator cannot be used for pointers
        which provides some advantages, but it is the opinion of the author that
        Dot operators should be use when possible for readability's sake
*/

struct matrix read_matrix(FILE* matrixfile)
{
    // Reads in matrix information and fills matrix struct
    // Read in N rows and M columns
    int N, M;
    fscanf(matrixfile, "%d", &N);
    fscanf(matrixfile, "%d", &M);

    // Create our matrix with empty elements
    struct matrix A = new_matrix(N, M);

    // Read in matrix values
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            fscanf(matrixfile, "%lf", &A.values[i][j]);
        }
    }

    return A;
}


struct matrix add(struct matrix A, struct matrix B)
{
    // Element-wise addition between 2 matrices and return the resulting matrix

    // Check that dimensions are equal
    if (A.N != B.N || A.M != B.M) {
        printf("Dimensions of A and B are not equal!\n");
        exit(1);
    }

    // C = A + B
    struct matrix C = new_matrix(A.N, A.M);

    for (int i = 0; i < A.N; i++) {
        for (int j = 0; j < A.M; j++) {
            C.values[i][j] =  A.values[i][j] + B.values[i][j];
        }
    }

    return C;
}


void print(struct matrix A, char* msg)
{
    // Convenient matrix print with message
    printf("%s\n", msg);
    for (int i = 0; i < A.N; i++) {
        for (int j = 0; j < A.M; j++) {
            printf("%5.2lf", A.values[i][j]);
        }
        printf("\n");
    }
}
