#include <iostream>
#include <fstream>

using namespace std;


int main()
{
    char str[10];

    // Create instance of ofstream and open foo.txt output file stream
    ofstream a_file ("foo.txt");
    // Output to foo.txt
    a_file << "0123456789! foo bar baz";
    // Close the file stream
    a_file.close();

    // Create instance of ifstream, and open foo.txt input file stream
    ifstream b_file("foo.txt");
    // Read a string from file (only 10 characters?)
    b_file  >> str;
    // Output
    cout << str << "\n";

    // Same thing, but getting passed the filename as an array of chars
    const char * filename = "foo.txt";
    ifstream c_file(filename);
    c_file  >> str;
    cout << str << "\n";

    // wait for key input to end
    cin.get();

    // b_file implicitly closed rather than explicitly: b_file.close()

    return 0;
}
