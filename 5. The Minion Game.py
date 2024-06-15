def minion_game(string):
    vowels = ['U', 'E', 'O', 'A', 'I']
    grade1 = 0
    grade2 = 0
    for i in range(len(string)):
        if string[i] in vowels:
            grade1 += (len(string) - i)
        else:
            grade2 += (len(string) - i)
    if grade1 > grade2:
        print('Kevin ' + str(grade1))
    elif grade1 < grade2:
        print('Stuart ' + str(grade2))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)