#!/bin/python3

import math
import os
import random
import re
import sys


#
# Write your code here
class comp:
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def add(self, other):
        self.real + other.real
        self.imag + other.imag
        result = (((str(self.real + other.real) + "+" + str(self.imag + other.imag) + "i")))
        # print(complex(self.real + other.real, self.imag + other.imag))
        print("Sum of the two Complex numbers :{}".format(result))

    def sub(self, other):
        # print(complex(self.real - other.real,self.imag - other.imag))
        # print("Subtraction of the two Complex numbers :{}".format(bcd))
        # print(self.real)
        # print(self.imag)
        # print(other.real)
        # print(other.real)
       # result = (((str(self.real - other.real) + str(self.imag - other.imag) + "i")))
        a = self.real - other.real
        b = self.imag - other.imag
        if a >= 0 or b >= 0:
            result = (((str(self.real - other.real) + "+" + str(self.imag - other.imag) + "i")))
        else:
            result = (((str(self.real - other.real) + str(self.imag - other.imag) + "i")))

        print("Subtraction of the two Complex numbers :{}".format(result))


if __name__ == '__main__':
    real1 = int(input().strip())
    img1 = int(input().strip())

    real2 = int(input().strip())
    img2 = int(input().strip())

    p1 = comp(real1, img1)
    p2 = comp(real2, img2)

    p1.add(p2)
    p1.sub(p2)
