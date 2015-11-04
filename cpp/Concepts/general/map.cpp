#include <map>
#include <iostream>
#include "map.h"

using namespace std;
map<string, string> gEnv;

int main() {

    populateMap(gEnv);

    cout << "Env[CHPL_HOME] = " << gEnv["CHPL_HOME"] << endl << endl;

    cout << "Env size: " << gEnv.size() << endl;

    for( map<string, string>::iterator ii=gEnv.begin(); ii!=gEnv.end(); ++ii)
    {
        cout << (*ii).first << ": " << (*ii).second << endl;
    }

    usemap();

    return 0;
}


void populateMap(map<string, string> &env)
{
    // Pass env by reference (no copy made)

    env["CHPL_HOME"] = "/Users/balbrecht/opt/dev/chapel/chapel";
    env["CHPL_COMM"] = "none";
}
