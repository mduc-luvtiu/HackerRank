from collections import deque

d = deque()
n = int(input())
for i in range(n):
    test = input().split()
    if test[0] == 'pop':
        d.pop()
    elif test[0] == 'popleft':
        d.popleft()
    elif test[0] == 'append':
        d.append(int(test[1]))
    elif test[0] == 'appendleft':
        d.appendleft(int(test[1]))

for i in d:
    print(i, end=' ')