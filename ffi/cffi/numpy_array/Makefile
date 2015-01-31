clang:
	gcc -c -Wall -Werror -fpic copy.c
	gcc -shared -o libcopy.so copy.o
gcc:
	gcc -c -std=c99 -Wall -Werror -fpic copy.c
	gcc -shared -std=c99 -o libcopy.so copy.o
icc:
	icc -c -Wall -Werror -fpic copy.c
	icc -shared -o libcopy.so copy.o
