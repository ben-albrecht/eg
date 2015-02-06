
//
// print.cpp
//

#include <iostream>
#include <fstream>

void Read(std::ifstream& finp);

extern "C"
{
    void ReadWrapper(const char * filename)
    {
        std::ifstream finp(filename);
        Read(finp);
    }
}

void Read(std::ifstream& finp)
{
    char str[20];

    finp >> str;

    std::cout << str << std::endl;
}

