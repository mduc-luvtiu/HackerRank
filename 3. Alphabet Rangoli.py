def print_rangoli(size):
    # width
    width = 4*size - 3
    # print top
    for i in range(1, size + 1):
        out = []
        for j in range(1, 2*i):
            out.append(chr(abs(i-j) + ord('a') + size - i))
        print('-'.join(out).center(width, '-'))
    # bottom
    for i in range(1, size)[::-1]:
        out = []
        for j in range(1, 2*i):
            out.append(chr(abs(i-j) + ord('a') + size - i))
        print('-'.join(out).center(width, '-'))



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)