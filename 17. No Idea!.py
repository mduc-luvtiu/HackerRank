if __name__ == '__main__':
    n , m = [int(i) for i in input().split()]
    arr = list([int(i) for i in input().split()])
    setA = set(int(i) for i in input().split())
    setB = set(int(i) for i in input().split())
    res = 0
    for i in arr:
        if i in setA:
            res += 1
        if i in setB:
            res -= 1
    print(res)
