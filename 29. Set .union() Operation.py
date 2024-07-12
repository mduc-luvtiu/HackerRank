a = int(input())

arr_a = [int(i) for i in input().split()]

b = int(input())

arr_b = [int(i) for i in input().split()]

res = set(arr_a)
print(len(res.union(arr_b)))
