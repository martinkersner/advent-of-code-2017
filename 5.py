import sys

input_file = sys.argv[1]

L = []
step_num = 0

with open(input_file, "r") as f:
    for line in f:
        L.append(int(line.strip()))

ci = 0
while True:
    offset = L[ci]
    step_num += 1
    if offset >= 3:
        L[ci] -= 1
    else:
        L[ci] += 1
    if (ci + offset) < 0 or (ci + offset) >= len(L):
        break
    ci += offset

print(step_num)
