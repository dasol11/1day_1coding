import sys

input = sys.stdin.readline

N = int(input())

stk = [0] * 1000001

stk[1] = 1
stk[2] = 2

for i in range(3,N+1):
    stk[i] = stk[i-1] + stk[i-2]
    
print(stk[N]%15746)
