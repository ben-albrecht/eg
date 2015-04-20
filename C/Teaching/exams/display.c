#include <stdio.h>

#define MAXSIZE 20

void displaylist(int *vec, int pvecsize) {
    for (int i = 0; i < pvecsize; i++) {
        printf("vec[%d] = %d\n", i, vec[i]);
    }
}

void getdata( int vec[], int *pvecsize )
{ // begin getdata
     // variable declaration
     int flag=1;
     // algorithm
     *pvecsize = 0;
     do
     { // begin do..while
        if ( flag == 1 );
        { // begin if
            printf( "\nEnter value ==> " );
            scanf( "%d", &vec[*pvecsize] );
            *pvecsize = *pvecsize+1;
        } // end if
            printf( "\nEnter another value? 1 = yes, 2 = no ==> " );
            scanf( "%d", &flag );
     } while ( flag == 1 );
} // end getdata


int main() {
    int vec[MAXSIZE];
    int pvecsize;
    getdata(vec, &pvecsize);
    displaylist(vec, pvecsize);

    return 0;

}
