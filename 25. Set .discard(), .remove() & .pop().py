n = int(input())

set_n = set([int(i) for i in input().split()])

N = int(input())

for i in range(N):
    commmand = input().split()
    if commmand[0] == 'pop':
        set_n.pop()
    elif commmand[0] == 'remove':
        set_n.remove(int(commmand[1]))
    elif commmand[0] == 'discard':
        set_n.discard(int(commmand[1]))

print(sum(set_n))