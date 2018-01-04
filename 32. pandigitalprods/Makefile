NAME=pandigitalprods

all: ${NAME}

${NAME}: ${NAME}.cpp
	g++ --pedantic -Wall -std=c++11 -O3 -o $@ $<

clean:
	-rm -f ${NAME}
