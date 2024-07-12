# Run with pypy3

import re

res = []
for i in range(int(input())):
    test = input()
    try:
        re.compile(test)
        res.append(True)
    except re.error:
        res.append(False)

for i in res:
    print(i)