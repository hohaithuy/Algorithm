#https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    tick = [0] * n
    ans = 0
    for i in range(n):
        if tick[i] == 1: continue
        if arr[i] == i + 1: tick[i] = 1
        else:
            current = arr[i]
            while(tick[i] != 1):
                if arr[current - 1] == i + 1:
                    tick[i] = 1
                    tick[current - 1] = 1
                else:
                    tick[current - 1] = 1
                    current = arr[current - 1]
                ans += 1
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
