n = int(input())

res = dict()
for i in range(n):
    test = input()
    res[test] = res.get(test, 0) + 1

print(len(res.keys()))
for i in res.keys():
    print(res[i], end=' ')