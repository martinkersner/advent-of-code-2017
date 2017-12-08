import sys

register = {}


def resolve(name):
    if not name.isdigit() and name[0] != "-":
        if register.get(name) is None:
            register[name] = 0
        return str(register[name])
    else:
        return name

def process_instruction(instruction):
    dst, op, val, _, lo, cnd, ro = instruction.strip().split(" ")

    val = int(val)

    if register.get(dst) is None:
        register[dst] = 0

    lo = resolve(lo)
    ro = resolve(ro)

    if eval("{} {} {}".format(lo, cnd, ro)):
        if op == "inc":
            register[dst] += val
        elif op == "dec":
            register[dst] -= val
        else:
            print("ERROR")


with open(sys.argv[1], "r") as f:
    for instruction in f:
        process_instruction(instruction)

max_v = 0
max_k = ""
for k, v in register.items():
    if v >= max_v:
        max_v = v
        max_k = k

print(max_k, max_v)
