#ifndef MAP_H
#define MAP_H

#include <map>

int main();

void populateMap(std::map<std::string, std::string> &env);

//Global
extern std::map<std::string, std::string> gEnv;

void usemap();

#endif
