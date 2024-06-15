import itertools

if __name__ == "__main__":
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    print(*list(itertools.product(A, B)))