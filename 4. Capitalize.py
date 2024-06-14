#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    res = chr(ord(s[0])-32) if 'a' <= s[0] <= 'z' else s[0]
    for i in range(1, len(s)):
        if s[i-1] == ' ' and 'a' <= s[i] <= 'z':
            res += chr(ord(s[i])-32)
        else:
            res += s[i]
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
