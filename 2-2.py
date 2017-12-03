import sys
import numpy as np


input_file = sys.argv[1]
sum = 0

with open(input_file, "r") as f:
    for line in f:
        a = [int(i) for i in line.strip().split()]
        s = np.matrix(sorted(a))
        m = s.T/s
        sum += max([r for r in m.flatten().tolist()[0] if r.is_integer()])

print(sum)
