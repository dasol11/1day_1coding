import sys
from collections import deque
input  = sys.stdin.readline

N = int(input())
que = deque()
for _ in range(N):
    li = list(map(int, input().split()))
    
    if li[0] == 1:
        que.appendleft(li[1])
    if li[0] == 2:
        que.append(li[1])
        
    if li[0] == 3:
        if que:
            print(que.popleft())
        else:
            print(-1)
            
    if li[0] == 4:
        if que:
            print(que.pop())
        else:
            print(-1)
    if li[0] == 5:
        print(len(que))
    if li[0] == 6:
        if que:
            print(0)
        else:
            print(1)
    if li[0] == 7:
        if que:
            print(que[0])
        else:
            print(-1)
            
    if li[0] == 8:
        if que:
            print(que[-1])
        else:
            print(-1)