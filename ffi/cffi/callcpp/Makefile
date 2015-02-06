all:
	g++ -c read.cpp -o read.o
	g++ -c main.c -o main.o
	g++ main.o read.o -o main

lib:
	g++ -shared -fPIC read.cpp -o libread.so
