from itertools import combinations
n = int(input())
char_n = input().split()
k = int(input())
m = combinations(char_n, k)
length = 0
count = 0
for i in m:
    length += 1
    if 'a' in i:
        count += 1

print('{:.4f}'.format(count/length))



