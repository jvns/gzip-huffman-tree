import sys


def print_codes(lengths):
    """
    Print a Huffman tree given pairs of characters and Huffman lengths.
    For instance:
    a, 3
    b, 3
    c, 4
    will output
    100
    101
    1100
    """
    last_code = None
    last_length = None
    for char, length in lengths:
        if last_code is None:
            code = 0
        else:
            if last_length == length:
                code = last_code + 1
            else:
                # Figure out what the first code for each bit-length would
                # be. This is one more than the last code of the previous
                # bit length, left-shifted once.
                code = (last_code + 1) << 1
        last_code = code
        last_length = length
        print "%04s" % repr(char), bin(code)[2:].zfill(length)


def read_lengths(infgen_output):
    lines = (l for l in infgen_output if 'litlen' in l)
    lines = (l.split() for l in lines)
    lines = ((int(code), int(length)) for _, code, length in lines)
    # Filter out anything where the code isn't ascii
    lines = ((chr(code), length) for code, length in lines if code < 256)
    return list(lines)

if __name__ == "__main__":
    lengths = read_lengths(sys.stdin)
    lengths.sort(key=lambda x: x[1])
    print_codes(lengths)
