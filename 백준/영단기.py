import sys

input = sys.stdin.readline

n, m = map(int,input().split())
dic = {}
for _ in range(n):
    st = input().rstrip()
    if len(st) >= m:
        if st in dic:
            dic[st] += 1
        else:
            dic[st] = 1

a = sorted(dic.items() , key= lambda x:( -(x[1]),-(len(x[0])) ))
for i in a:
    print(i[0])
    