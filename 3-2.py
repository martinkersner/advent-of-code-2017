# ugly but correct

import numpy as np
import math

input = 368078

s = math.ceil(math.sqrt(input))
A = np.zeros((s,s), dtype=np.uint32)

center_row = int(A.shape[0]/2)
center_col = int(A.shape[1]/2)

A[center_row,center_col] = 1

row = center_row
col = center_col + 1

step_num = 2
state = "UP"

def sum_neighborhood(M, row, col):
    return M[row, col-1] + \
           M[row-1, col] + \
           M[row, col+1] + \
           M[row+1, col] + \
           M[row-1, col+1] + \
           M[row+1, col-1] + \
           M[row-1, col-1] + \
           M[row+1, col+1]

def is_end(val):
    if val > input:
        print(val)
        exit()

while True:
    if state == "UP":
        step_tmp = step_num
        while step_tmp > 0:
            A[row, col] = sum_neighborhood(A, row, col)
            is_end(A[row, col])
            row -= 1
            step_tmp -= 1
        row += 1
        col -= 1
        state = "LEFT"
        continue

    if state == "LEFT":
        step_tmp = step_num
        while step_tmp > 0:
            A[row, col] = sum_neighborhood(A, row, col)
            is_end(A[row, col])
            col -= 1
            step_tmp -= 1
        row += 1
        col += 1
        state = "DOWN"
        continue

    if state == "DOWN":
        step_tmp = step_num
        while step_tmp > 0:
            A[row, col] = sum_neighborhood(A, row, col)
            is_end(A[row, col])
            row += 1
            step_tmp -= 1
        col += 1
        row -= 1
        state = "RIGHT"
        continue

    if state == "RIGHT":
        step_tmp = step_num
        while step_tmp > 0:
            A[row, col] = sum_neighborhood(A, row, col)
            is_end(A[row, col])
            col += 1
            step_tmp -= 1
        step_num += 2
        state = "UP"
        continue
