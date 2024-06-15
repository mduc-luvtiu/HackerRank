import collections

if __name__ == "__main__":
    x = int(input())
    lst = [int(i) for i in input().split()]
    n = int(input())
    info = []
    for i in range(n):
        a = [int(i) for i in input().split()]
        info.append(a)
    dic = collections.Counter(lst)
    res = 0
    for i in range(n):
        if (info[i][0] in dic.keys()) and (dic[info[i][0]]>0):
           res += info[i][1]
           dic[info[i][0]] -= 1
    print(res)

