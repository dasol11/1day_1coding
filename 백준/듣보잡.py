import sys

input = sys.stdin.readline
n, m =map(int,input().split())
dic1  ={}
for _ in range(n):
    s = str(input().strip())
    dic1[s] = 0
dic2 = {}
for _ in range(m):
    s = str(input().strip())
    if s in dic1:
        dic2[s] = 0

stk = sorted(list(dic2.keys()))
print(len(stk))
for i in stk:
    print(i)
