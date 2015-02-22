import sys
import subprocess


def generate_codes(lengths):
    last_code = None
    last_length = None
    for char, length in lengths:
        if last_code is None:
            code = 1 << length
        else:
            if last_length == length:
                code = last_code + 1
            else:
                code = (last_code + 1) << 1
        last_code = code
        last_length = length
        print "%06s" % repr(char), bin(code)[2:]


def read_lengths(infgen_output):
    lines = []
    for line in infgen_output:
        if 'litlen' not in line:
            continue
        asciicode, length = line.strip().split()[1:]
        character = int(asciicode)
        if character >= 256:
            continue
        character = chr(character)
        length = int(length)
        lines.append((character, length))
    return lines

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "You need a filename!"
        sys.exit(0)
    filename = sys.argv[1]
    try:
        infgen_output = subprocess.check_output(['./infgen', filename]).split("\n")
    except OSError:
        print "./infgen not found. Maybe try running `make`?"
        sys.exit(0)
    lengths = read_lengths(infgen_output)
    lengths.sort(key=lambda x: x[1])
    generate_codes(lengths)
