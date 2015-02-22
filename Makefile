infgen.c:
	wget http://zlib.net/infgen.c.gz
	gunzip infgen.c.gz

all: infgen.c
	gcc -o infgen infgen.c
