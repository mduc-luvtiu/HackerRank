from collections import OrderedDict

if __name__ == "__main__":
    n = int(input())
    res = OrderedDict()
    for i in range(n):
        item = input().split()
        name = ' '.join(item[:-1])
        price = int(item[-1])
        if name in res.keys():
            res[name] += price
        else:
            res[name] = price
    for i in res.keys():
        print(f"{i} {res[i]}")
