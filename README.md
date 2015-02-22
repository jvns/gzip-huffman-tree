# huffman fun

This hacky Python script prints out the Huffman tree for the first block
in a gzip file.

It uses a program called `infgen` available from
http://zlib.net/infgen.c.gz. The Makefile here will download and compile
it for you, though!

To try this out on the included gzip file, run

```
$ make
$ ./infgen raven.txt.gz | python print_huffman_table.py
```

You should see output like this:


```
 ' ' 00000
 'a' 00001
 'e' 00010
 'i' 00011
 'n' 00100
 'o' 00101
 'r' 00110
 's' 00111
 't' 01000
'\n' 010010
 ',' 010011
 'b' 010100
 'c' 010101
 'd' 010110
 'f' 010111
 'h' 011000
 'l' 011001
 'm' 011010
 'p' 011011
 'u' 011100
 'g' 0111010
 'w' 0111011
 'y' 0111100
 "'" 01111010
 'I' 01111011
 'O' 01111100
 'S' 01111101
 'T' 01111110
 '`' 01111111
 'k' 10000000
 'v' 10000001
 '!' 100000100
 '-' 100000101
 '.' 100000110
 ';' 100000111
 'A' 100001000
 'B' 100001001
 'D' 100001010
 'F' 100001011
 'G' 100001100
 'M' 100001101
 'N' 100001110
 'P' 100001111
 'W' 100010000
 '"' 1000100010
 '?' 1000100011
 'C' 1000100100
 'E' 1000100101
 'L' 1000100110
 'q' 1000100111
 'H' 10001010000
 'Q' 10001010001
 'R' 10001010010
 'j' 10001010011
 'x' 10001010100
```
