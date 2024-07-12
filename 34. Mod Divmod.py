def divmod(a, b):
    return (a//b, a%b)

a = int(input())
b = int(input())
tup = divmod(a, b)
print(tup[0])
print(tup[1])
print(tup)