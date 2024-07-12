n = int(input())
arr_n = [int(i) for i in input().split()]
m = int(input())
arr_m = [int(i) for i in input().split()]

print(len(set(arr_m).intersection(arr_n)))