def bin(n):
    res = ''
    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res

def oct(n):
    res = ''
    while n > 0:
        res = str(n % 8) + res
        n //= 8
    return res

def hex(n):
    res = ''
    hexchar = '0123456789ABCDEF'
    while n > 0:
        res = hexchar[n % 16] + res
        n //= 16
    return res


def print_formatted(number):
    width = len(bin(number))
    for i in range(1, number + 1):
        print(str(i).rjust(width), oct(i).rjust(width), hex(i).rjust(width), bin(i).rjust(width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
