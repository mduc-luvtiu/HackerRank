from collections import defaultdict

def appearance(lst1 : [], lst2 : []):
    d = defaultdict(list)
    for i in range(len(lst2)):
        if lst2[i] not in lst1:
            d[i].append(-1)
            continue
        for j in range(len(lst1)):
            if lst1[j] == lst2[i]:
                d[i].append(j+1)
    for i in d.keys():
        print(*d[i])

if __name__ == "__main__":
    n , m = map(int, input().split())
    lst_n = []
    lst_m = []
    for i in range(n):
        lst_n.append(input())
    for j in range(m):
        lst_m.append(input())
    appearance(lst_n, lst_m)
