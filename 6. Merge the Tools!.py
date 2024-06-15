def merge_the_tools(string, k):
    s = [string[k*i:k*(i+1)] for i in range(len(string)//k)]
    res = []
    for i in range(len(s)):
        res.append('')
        for j in s[i]:
           if j not in res[i]:
               res[i] += j
    for i in range(len(res)):
        print(res[i])


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)