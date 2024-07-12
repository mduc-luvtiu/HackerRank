from collections import deque

t = int(input())
for i in range(t):
    n = int(input())
    arr_n = deque()
    for x in input().split():
        arr_n.append(int(x))
    res = [max(arr_n[0], arr_n[-1])]
    while len(arr_n) > 0:
        if arr_n[0]>arr_n[-1]:
            if arr_n[0]<=res[-1]:
                res.append(arr_n[0])
                arr_n.popleft()
            else:
                check = 'No'
                break
        else:
            if arr_n[-1]<=res[-1]:
                res.append(arr_n[-1])
                arr_n.pop()
            else:
                check = 'No'
                break
    else:
        check = 'Yes'

    print(check)

