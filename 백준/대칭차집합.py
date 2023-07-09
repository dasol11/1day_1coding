import sys

input = sys.stdin.readline
n, m =map(int,input().split())

set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))

stk = []
stk.append(set1-set2)
stk.append(set2-set1)
print(len(stk[0])+len(stk[1]))