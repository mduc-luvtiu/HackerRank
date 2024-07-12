from itertools import combinations_with_replacement

s = input()

s_split = s.split()
letter = [i for i in s_split[0]]
letter.sort()
lst = combinations_with_replacement(letter, int(s_split[1]))
for i in lst:
    print(''.join(i))