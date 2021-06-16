#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/fair-rations/problem
#

def fairRations(B):
    n = len(B)

    count = 0
    for i in range(n):
        if B[i] % 2 == 0: continue
        else:
            if i == n - 1: return "NO"
            B[i + 1] += 1
            count += 2

    return str(count)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
