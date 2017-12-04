import sys
import hashlib

def hash(string):
    b = bytearray()
    b.extend(string.encode())
    return hashlib.sha224(b).hexdigest()


valid = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        input = line.strip().split()
        output = set([hash(s) for s in input])
        if len(input) == len(output):
            valid += 1

print(valid)
