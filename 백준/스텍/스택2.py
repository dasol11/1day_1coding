import sys

input  = sys.stdin.readline

N = int(input())
stk = []
for _ in range(N):
    li = list(map(int, input().split()))
    
    if li[0] == 1 :
        stk.append(li[1])
    if li[0] == 2 :
        if stk:
            print(stk.pop())
        else:
            print(-1)
    if li[0] == 3:
        print(len(stk))
    if li[0] == 4:
        if stk:
            print(0)
        else:
            print(1)
    if li[0] == 5:
        if stk:
            print(stk[-1])
        else:
            print(-1)
        
    