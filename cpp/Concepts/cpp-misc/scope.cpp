#include <stdio.h>

int foo = 1;

void printbar(int bar) {
    printf("%d\n", bar);
}

int main()
{
  int bar = 2;
  printf("Hello World\n");
  printf("%d\n", foo);
  printbar(bar);
}
