#include<iostream>
#include "fib.h"

using namespace std;

int fib()
{
    int n = 5;
    int c, first = 0, second = 1, fib;

        //cout << "First " << n << " terms of Fibonacci series are :- " << endl;

        for ( c = 0 ; c < n ; c++ )
        {
           if ( c <= 1 )
              fib = c;
           else
           {
              fib = first + second;
              first = second;
              second = fib;
           }
           //cout << fib << endl;
        }

   return fib;
}

int main(int argc, char *argv[])
{
    if ( argc != 2 ) {
        printf("Usage: fib(n)\n");
        return 1;

    }
    else {
        int n = stoi(argv[1]);
        fib();
    }
    return 0;
}
