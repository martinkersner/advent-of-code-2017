import sys


input = sys.argv[1]
input += input[0]
sum = 0

previous = None
for current in input:
    if previous is not None:
        if current == previous:
            sum += int(current)

    previous = current

print(sum)
