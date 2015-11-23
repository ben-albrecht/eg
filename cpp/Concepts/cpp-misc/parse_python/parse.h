#ifndef PARSE_H
#define PARSE_H 1

#include <string>
#include <map>

int main();

std::string exec(std::string cmd);

std::map<std::string, const char*> populateMap(std::string);
#endif
