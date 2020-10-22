#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'FORLoop' function below.
#

def FORLoop():
    l1 = []
    n = int(input())
    for i in range(0, n):
        ab = int(input())
        l1.append(ab)
    print(l1)
    iter1 = iter(l1)
    while True:
        try:
            print(next(iter1))
        except StopIteration:
            break
    return iter1


if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))

    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')


