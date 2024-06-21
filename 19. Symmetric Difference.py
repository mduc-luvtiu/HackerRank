if __name__ == '__main__':
    m = int(input())
    arr_m = set(int(i) for i in input().split())
    n = int(input())
    arr_n = set(int(i) for i in input().split())
    dif = arr_n.difference(arr_m)
    dif.update(arr_m.difference(arr_n))
    res = list(dif)
    res.sort()
    for i in res:
        print(i)