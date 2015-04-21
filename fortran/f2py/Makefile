.PHONY: add, addprocedures, python

add:
	gfortran add.f90 -o add

addprocedures:
	gfortran -shared -fPIC -o addprocedures.so addprocedures.f90

python:
	f2py3.5 -c -m addprocedures addprocedures.f90
