#include <string>
#include <map>
#include <cstdio>
#include <iostream>

#include "parse.h"


int main()
{
    std::string make = "\0";
    // Call chplenv.py and collect output into string
    std::string command = "python chplenv.py 2>&1";
    std::string output = exec(command);

    // Parse output of chplenv.py and populate map with env vars
    std::map<std::string, const char*> env = populateMap(output);

    // Iterate over and print key/value pairs in map out for proof that it worked!
    for( std::map<std::string, const char*>::iterator ii=env.begin(); ii!=env.end(); ++ii)
    {
        make = (*ii).first;
        make.insert(5, "MAKE_");
        //std::cout << (*ii).first << ": " << (*ii).second << std::endl;
        std::cout << make << ": " << (*ii).second << std::endl;
    }

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


std::map<std::string, const char*> populateMap(std::string output)
{
    // Destructively parses string output for environment variables (keys)
    // and their values according to printchplenv (values), and returns an
    // std::map populated with the key/value pairs

    std::map<std::string, const char*> env;

    // Lines
    std::string line= "";
    std::string lineDelimiter = "\n";
    size_t linePos = 0;        // Line break position

    // Tokens
    std::string tokenDelimiter = "=";
    size_t delimiterPos = 0;    // Position of delimiter
    size_t valuePos = 0;        // Position of value

    std::string key = "";
    std::string value = "";

    while ((linePos = output.find(lineDelimiter)) != std::string::npos)
    {
        line = output.substr(0, linePos);

        // Key is substring up until "=" on a given line
        delimiterPos = line.find(tokenDelimiter);
        key = line.substr(0, delimiterPos);

        // value is substring up after "=" on a given line
        valuePos = delimiterPos + tokenDelimiter.length();
        value = line.substr(valuePos);

        // Populate map, duplicating string, because output is destroyed in memory
        env[key] = strdup(value.c_str());
        output.erase(0, linePos + lineDelimiter.length());
    }
    return env;
}

