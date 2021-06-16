#!/bin/python3

import math
import os
import random
import re
import sys


def linked(i, j, n, m, matrix, tick):
    count = 0
    if matrix[i][j] == 0: return 0
    elif tick[i][j] == 0:
        for l in range(-1, 2):
            for k in range(-1, 2):
                if l + i < 0 or l + i >= n or j + k < 0 or j + k >= m or (l == 0 and k == 0):
                    continue
                count += linked(l + i, j + k, n, m, matrix, tick)
        return 1 + count
    return 0
                

def connectedCell(n, m, matrix):
    tick = [[0] * m] * n
    res = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and tick[i][j] == 0:
                res = max(res, linked(i, j, n, m, matrix, tick))
    return res




n = int(input().strip())

m = int(input().strip())

matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

result = connectedCell(n, m, matrix)
print(result)
