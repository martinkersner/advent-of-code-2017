import sys


input_file = sys.argv[1]
sum = 0

with open(input_file, "r") as f:
    for line in f:
        a = [int(i) for i in line.strip().split()]
        sum += abs(min(a)-(max(a)))

print(sum)
