# better not look
import sys
import numpy as np
import copy


def parse(line):
    line = line.strip()
    line_split = line.split()
    name = line_split[0]
    weight = int(line_split[1][1:-1])
    descendents = []
    if len(line_split) >= 3:
        descendents = [i.replace(",", "") for i in line_split[3:]]

    return name, weight, descendents


towers = {}
with open(sys.argv[1], "r") as f:
    for line in f:
        # print(parse(line))
        name, weight, descendents = parse(line)
        towers[name] = {"w": weight, "d": descendents}


main = []
desc = []

for k, v in towers.items():
    if len(v["d"]) > 0:
        main.append(k)
        desc.extend(v["d"])

root = list(set(main)-set(desc))[0]

state = [(root, 0)]

aaa = {}
max_l = 0
while True:
    if state == []:
        break

    c = state.pop()
    n,l = c

    if l > max_l:
        max_l = l

    new_state = [(nn, l+1) for nn in towers[n]["d"]]
    for nn in towers[n]["d"]:
        if aaa.get(l+1):
            if aaa[l+1].get(n):
                aaa[l+1][n].append(nn)
            else:
                aaa[l+1][n] = [nn]
        else:
            aaa[l+1] = {}
            aaa[l+1][n] = [nn]

    state = new_state + state

bbb = copy.deepcopy(towers)

for i in [5, 4, 3]:
    print(i)
    tmp_list = []
    tmptmptmp = []
    for k,v in aaa[i].items():
        tmptmp = []
        for vv in v:
            tmptmp.append(towers[vv]["w"])
            # print(vv)

        # print("k", k)
        # print(tmptmp)
        # print(set(tmptmp))
        # print()
        towers[k]["w"] += np.sum(tmptmp)
    # print()

print(bbb["gexwzw"]["w"])
