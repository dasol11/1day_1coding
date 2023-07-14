
import sys

input = sys.stdin.readline

T = int(input())
stk =[]
for _ in range(T):
    s = int(input())
    if s == 0:
        stk.pop()
    else:
        stk.append(s)
        
print(sum(stk))