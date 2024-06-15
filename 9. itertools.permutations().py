import itertools

if __name__ == "__main__":
    s, k = [i for i in input().split()]
    s = [i for i in s]
    s.sort()
    k = int(k)
    lst = list(itertools.permutations(s, k))
    check = []
    for i in lst:
        if i not in check:
            print(*i, sep='')
            check.append(i)