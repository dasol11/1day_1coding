import sys

input = sys.stdin.readline

N = int(input())

stk = [0] *10001

for _ in range(N):
    tmp = int(input())
    stk[tmp] += 1

for i in range(10001):
    if stk[i] !=0:
        for j in range(stk[i]):
            print(j)