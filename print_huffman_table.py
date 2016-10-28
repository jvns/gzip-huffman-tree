import sys


def print_codes(lengths):

    # MAX_BITS = 15 -> maximum number of bits for code lengths
    # bl_count stores how many codes are found for each symbol ASCII code
    min_length = 15 
    bl_count = [0] * 16 
    for lines in lengths:
         bl_count[lines[1]-1]+=1 
         if min_length > lines[1]:
                min_length = lines[1]


    # next_code contains the first code at each length change(eg. from 4 to 5 bits)
    next_code = [0] * 16
    code = 0

    for bits in range(1,16):
        code = ( code + bl_count[ bits - 1 ] ) << 1
        if  bl_count[ bits ]:
                next_code[ bits ] = code

    print "Huffman tree code lengths:"
    print "========================="
    for bits in range(min_length,16):
        print bits,bin(next_code[bits-1])[2:].zfill(min_length)
    print "========================="



    # There are 2 sorting ways: by Symbol ASCII CODE or by somb code length.
    # Only one method can be activated in the code.

    '''
    # Sort by Symbol ASCII code
    for lines in lengths:
        bits = lines[1]
        if lines[0] < 256:
                print "%04s" % repr(chr(lines[0])), bin(next_code[bits-1])[2:].zfill(min_length)
        next_code[bits-1] +=1
    '''

    # Sort by symbol code length
    for current_bits in range(min_length,16):
        for lines in lengths:
                bits = lines[1]
                if lines[0] < 256 and bits == current_bits:
                        print "%06s" % repr(chr(lines[0])), bin(next_code[bits-1])[2:].zfill(min_length)
                if bits == current_bits:
                        next_code[bits-1] +=1


def read_lengths(infgen_output):

    # DEFLATE stream contains one or more blocks . Process one block at a time.
    # Otherwise codes and lengths get mangled.
    # Different blocks have different code lengths.

    blockslist = []
    blocklines = []
    for line in infgen_output:
	if line.startswith('end'):  # All blocks should have an "end" directive , otherwise this will fail
		blockslist.append (blocklines)	
		blocklines = []
	elif 'litlen' in line:
		split = line.split()
		blocklines.append( (int(split[1]),int(split[2])) )
    return blockslist



if __name__ == "__main__":
    ''' 
    DEFLATE algorithm dissector
    See: https://jvns.ca/blog/2015/02/22/how-gzip-uses-huffman-coding/
	 http://www.infinitepartitions.com/art001.html

   '''

    blockslist = read_lengths(sys.stdin)
    block_no = 0

    for blocks in blockslist:
	block_no += 1
	print "Block number = ", block_no
	print "========================="
        print_codes(blocks)
	print "\n"
    
    print "Number of blocks = ", block_no
