if __name__ == "__main__":
    lst_test = []
    t = int(input())
    for i in range(t):
        lst_test.append(input().split())

    for i in lst_test:
        try:
            a = int(i[0])
        except:
            print(f'Error Code: invalid literal for int() with base 10: \'{i[0]}\'')
            continue

        try:
            b = int(i[1])
        except:
            print(f'Error Code: invalid literal for int() with base 10: \'{i[1]}\'')
            continue


        try:
            print(a//b)
        except:
            print('Error Code: integer division or modulo by zero')
            continue

