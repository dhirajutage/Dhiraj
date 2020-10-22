# Hello World program in Python

import math
import os
import random
import re
import sys

length = int(input().strip())

qw1 = []
for i in range(length):
    qw2 = []
    for _ in range(length):
        qw2_item = (input().strip())
        qw2.append(qw2_item)
        qw1.append(tuple(qw2))
tupb = tuple(qw1)
print(tupb)