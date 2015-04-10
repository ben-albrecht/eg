#include <stdio.h>  // printf(), scanf()
#include <stdlib.h> // exit()
#include <ctype.h>  // toupper()

int sumfunc(int* , int);
int minfunc(int* , int);
int maxfunc(int* , int);

int main() {

    char response;

    //1. Option to read in matrix from file (matrix.dat) or input matrix elements manually
    for(;;){
        printf("What would you like to do?\n\
                [R]ead in matrix from 'matrix.dat'\n\
                [I]nput it yourself\n");
        scanf(" %c", &response);
        response = toupper(response);
        if (response == 'R' || response == 'I') break;
        else printf("Please enter 'R' or 'I'\n");
    }

    int const dim = 4;
    int matrix[dim][dim];
    if (response == 'R') {
        // Read matrix from matrix.dat
        FILE *matrixfile = fopen("matrix.dat", "r");
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                fscanf(matrixfile, "%d", &matrix[i][j]);
            }
        }
    }
    else {
        // Allow user to input matrix
        printf("\n");
        for (int i = 0; i < dim; i++) {
            for (int j = 0; j < dim; j++) {
                printf("matrix[%d][%d] = ", i, j);
                scanf("%d", &matrix[i][j]);
                printf("\n");
            }
            printf("\n");
        }
    }

    printf("The inputted matrix looks like:\n\n");
    for (int i = 0; i < dim; i++) {
        for (int j = 0; j < dim; j++) {
            printf("%3d ", matrix[i][j]);
        }
        printf("\n");
    }

    //2. Option(s) to operation sum, min, and max of given row, column, or diagonal

    /*
        MxN matrix
        =========
        sum     min      max
        row     column   diagonal
        m_idx   n_idx
    */


    char operation;
    for(;;) {
        printf("What would you like to operation?\n");
        printf("[S]um\n");
        printf("[M]aximum\n");
        printf("[m]inimum\n");
        scanf(" %c", &operation);
        if (operation == 'm' || operation == 'M' || operation == 'S') break;
        else printf("Please enter 'S', 'M', or 'm'\n");
    }

    char elements;
    for(;;) {
        printf("What part of the matrix would you like to operation?\n");
        printf("[R]ow\n");
        printf("[C]column\n");
        printf("[D]iagonal\n");
        scanf(" %c", &elements);
        elements = toupper(elements);
        if (elements == 'R' || elements == 'C' || elements == 'D') break;
        else printf("Please enter 'R', 'C', or 'D'\n");
    }


        int index;
        if (elements == 'R' || elements == 'C') {
            for(;;) {
                printf("Which index?\n");
                scanf(" %d", &index);
                if (index < dim && index >= 0) break;
                else printf("Please pick a value between 0 and %d", dim);
            }
        }


        // Matrix -> array depending on elements
        int array[dim];
        switch(elements) {
            case 'R':
                // Set array to that row
                for (int j = 0; j < dim; j++) {
                    array[j] = matrix[index][j];
                }
                break;
            case 'C':
                // Set array to that column
                for (int i = 0; i < dim; i++) {
                    array[i] = matrix[i][index];
                }
                break;
            case 'D':
                // Set array to the diagonal
                for (int i = 0; i < dim; i++) {
                    array[i] = matrix[i][i];
                }
                break;
            default:
                printf("An error has occurred");
                exit(1);
        }


        int answer;
        switch(operation) {
            case 'S':
                answer = sumfunc(array, dim);
                break;
            case 'M':
                answer = maxfunc(array, dim);
                break;
            case 'm':
                answer = minfunc(array, dim);
                break;
            default:
                printf("An error has occurred");
                exit(1);
        }

    printf("\nAnswer=  %d\n", answer);
    return 0;
}



int minfunc(int *arr, int n) {
    int minimum = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < minimum) {
            minimum=arr[i];
        }
    }
    return minimum;
}


int maxfunc(int *arr, int n) {
    int maximum = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > maximum) {
            maximum = arr[i];
        }
    }
    return maximum;
}

int sumfunc(int *arr, int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return sum;
}
