#include <string>
#include <iostream>

int main()
{
  std::string result ="";
  std::string foo = "foo";
  const char* bar = "bar";

  result += foo + bar;

  std::cout << result << std::endl;

  return 0;
}
