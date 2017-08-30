PY = python
PYFLAGS =
DOC = doxygen
DOCFLAGS = 
DOCCONFIG = ./test.py

SRC = ./src/testCircles.py

.PHONY: all prog doc clean

prog:
	$(PY) $(PYFLAGS) $(DOCCONFIG)
	cd latex && $(MAKE)

all: prog doc

clean:
	rm -rf html
	rm -rf latex
