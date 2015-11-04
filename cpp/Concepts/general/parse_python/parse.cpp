#include <string>
#include <map>
#include <cstdio>
#include <iostream>

#include "parse.h"


int main()
{
    // Call chplenv.py
    std::string command = "python chplenv.py 2>&1";
    std::string output = exec(command);
    //printf("str: %s\n", output.c_str());

    // Parse output
    std::string delimiter = "\n";
    size_t pos = 0;
    std::string token;

    while ((pos = output.find(delimiter)) != std::string::npos)
    {

        token = output.substr(0, pos);
        std::cout << token << std::endl;
        output.erase(0, pos + delimiter.length());

    }

    // Feed output into map
    std::map<std::string, const char*> env;

    return 0;
}

std::string exec(std::string cmd) 
{
    FILE* pipe = popen(cmd.c_str(), "r");
    if (!pipe) return "ERROR";
    char buffer[128];
    std::string result = "";
    while (!feof(pipe)) {
        if (fgets(buffer, 128, pipe) != NULL)
            result += buffer;
    }
    pclose(pipe);
    return result;
}
