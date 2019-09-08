#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    max = sum(arr[1:])
    min = sum(arr[:-1])

    return min,max

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    min, max = miniMaxSum(arr)

    print("{0} {1}".format(min,max))

    print()
