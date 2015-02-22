# huffman fun

This hacky Python script prints out the Huffman tree for the first block
in a gzip file.

It uses a program called `infgen` available from http://zlib.net/infgen.c.gz

To try this out on the included gzip file, run

```
$ make
$ python print_huffman_table.py raven.txt.gz
```
