def next_side(L):
    length = int(len(L)/2)
    L2 = [i+2 for i in L[0:length]]
    L2.extend(L[length:])
    last = L2[-1]

    for i in range(2):
        last = L2[-1]
        L2.append(last+1)

    return L2


current_idx = 0
idx = 368078

L = [1, 2]
while True:
    if current_idx < idx:
        side = L * 4
        current_idx += len(side)
        L = next_side(L)
    else:
        print(side[abs(idx-current_idx)])
        break
