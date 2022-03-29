STEPS = build test

.PHONY: STEPS

test:
	python testing.py

build:
	cython -3 test3.py 
	cythonize --build --inplace test3.c
	nuitka --module test2.py

install:
	pip install cython nuitka