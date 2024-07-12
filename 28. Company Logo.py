#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    res = dict()
    s = input()
    for i in s:
        res[i] = res.get(i, 0) + 1
    value = list(set(res.values()))
    value.sort()
    key = list(res.keys())
    key.sort()
    count = 0
    for i in value[::-1]:
        if count == 3:
            break
        for j in key:
            if count == 3:
                break
            if res[j] == i:
                print(j, i)
                count += 1