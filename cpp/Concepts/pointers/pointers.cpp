//  File: pointers.cpp
//
//      1.0 The Basics
//      1.1 Arrays and pointers
//      2.0 Functions and pointers
//

// Includes
#include <iostream>
#include "pointers.h"

using namespace std;

int main ()
{

    // 1.0 The Basics
    // I like to think of the reference operator (&) as "the address of (pointer)"
    // and the dereference operator (*) as "the contents of (address)"

    int * a_ptr, * b_ptr;
    int alpha, beta;
    a_ptr = &alpha;

    *a_ptr = 10;

    b_ptr = &beta;
    *b_ptr = 20;
    cout << "alpha is " << alpha << endl; //10
    cout << "beta is " << beta << endl; //20

    // 2.0 Functions and Pointers
    //
    cout << "(*+) takes dereferenced integers as inputs" << endl;
    cout << "(&+) takes referenced integers as inputs" << endl;
    //
    cout << "alpha + beta = " << add(alpha, beta) << endl;
    cout << " * a_ptr + * b_ptr = " << add(* a_ptr, * b_ptr) << endl;
    //
    cout << " * a_ptr (&+) * b_ptr = " << add_ref(* a_ptr, * b_ptr) << endl;
    cout << " alpha (&+) beta = " << add_ref(alpha, beta) << endl;
    //
    cout << " a_ptr (*+) b_ptr = " << add_deref(a_ptr, b_ptr) << endl;
    cout << " & alpha (*+) & beta = " << add_deref(& alpha, & beta) << endl;



return 0;
}

// 2.0 Functions and Pointers
int add(int a, int b) // (+)
{
    return(a+b);
}

int add_deref(int * a, int * b) // (*+)
{

    return(* a + * b);
}

int add_ref(int & a, int & b) // ($+)
{

    return(  a +  b);
}
