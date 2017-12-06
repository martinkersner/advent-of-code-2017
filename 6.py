import sys
import numpy as np

with open(sys.argv[1], "r") as f:
    L = [int(i) for i in f.readline().strip().split("\t")]


def distribute(L, idx, val):
    while val > 0:
        if idx >= len(L):
            idx = 0
        L[idx] += 1
        idx += 1
        val -= 1

    return L


set_memory = set([])

i = 1
while True:
    idx = np.argmax(L)
    val = L[idx]
    L[idx] = 0
    distribute(L, idx+1, val)
    L_string = "".join([str(i) for i in L])
    size_before = len(set_memory)
    set_memory.add(L_string)
    size_after = len(set_memory)
    if size_before == size_after:
        print(i)
        break
    i += 1
