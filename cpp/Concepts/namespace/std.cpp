// Test setting only one function to namespace std::

#include <iostream>
#include <math.h>
// All std
//  using namespace std;
// Just cout:
//  #define cout std::cout
// Just cout (better):
using std::cout;
using std::isnan;

int main() {
    cout << "Hello World\n";
    int num;
    if isnan(num) printf("nan\n");
}
