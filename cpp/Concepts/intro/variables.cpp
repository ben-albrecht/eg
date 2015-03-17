#include <iostream>

using namespace std;

int main()
{
  // Declaring variable of type = integer, and name = thisisanumber
  int thisisanumber;

  cout<<"Please enter a number: ";

  cin>> thisisanumber;
  cin.ignore();
  cout<<"You entered: "<< thisisanumber <<"\n";
  cin.get();
}
