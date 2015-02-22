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
 ' ' 100000
 'a' 100001
 'e' 100010
 'i' 100011
 'n' 100100
 'o' 100101
 'r' 100110
 's' 100111
 't' 101000
'\n' 1010010
 ',' 1010011
 'b' 1010100
 'c' 1010101
 'd' 1010110
 'f' 1010111
 'h' 1011000
 'l' 1011001
 'm' 1011010
 'p' 1011011
 'u' 1011100
 'g' 10111010
 'w' 10111011
 'y' 10111100
 "'" 101111010
 'I' 101111011
 'O' 101111100
 'S' 101111101
 'T' 101111110
 '`' 101111111
 'k' 110000000
 'v' 110000001
 '!' 1100000100
 '-' 1100000101
 '.' 1100000110
 ';' 1100000111
 'A' 1100001000
 'B' 1100001001
 'D' 1100001010
 'F' 1100001011
 'G' 1100001100
 'M' 1100001101
 'N' 1100001110
 'P' 1100001111
 'W' 1100010000
 '"' 11000100010
 '?' 11000100011
 'C' 11000100100
 'E' 11000100101
 'L' 11000100110
 'q' 11000100111
 'H' 110001010000
 'Q' 110001010001
 'R' 110001010010
 'j' 110001010011
 'x' 110001010100
```
