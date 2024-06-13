'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
'''

N, M = [int(i) for i in input().split()]

for i in range(N//2):
    out = '.|.'*(2*i+1)
    print(out.center(M, '-'))

print('WELCOME'.center(M, '-'))

for i in range(N//2)[::-1]:
    out = '.|.'*(2*i+1)
    print(out.center(M, '-'))

