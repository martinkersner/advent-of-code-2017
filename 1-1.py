import sys


input = sys.argv[1]
sum = 0
length = len(input)
step = length/2
input += input[:-step+1]

previous = None
for idx, current in enumerate(input[:-step]):
    if previous is not None:
        if current == input[idx+step]:
            sum += int(current)

    previous = current

print(sum)
