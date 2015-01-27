all:
	gcc -c -Wall -Werror -fpic foo.c
	gcc -shared -o libfoo.so foo.o
	gcc -L/Users/albrecht/repos/eg/C/sharedlib -Wall -o test main.c -lfoo


