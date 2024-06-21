from itertools import combinations

if __name__ == '__main__':
    s , k = input().split()
    s = [i for i in s]
    s.sort()
    s = ''.join(s)
    k = int(k)
    for i in range(1, k+1):
        res = list(combinations(s, i))
        for j in res:
            print(''.join(j))

