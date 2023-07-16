import sys
import collections
input = sys.stdin.readline

N = int(input())
que = collections.deque()
for _ in range(N):
    s = input().split()
    
    if s[0] == "push":
        que.append(s[1])
        
    elif s[0] == "pop":
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(que))
        
    elif s[0] == "empty":
        if que:
            print(0)
        else:
            print(1)
    elif s[0] == "front":
        if que:
            print(que[0])
        else:
            print(-1)
    elif s[0] == "back":
        if que:
            print(que[-1])
        else:
            print(-1)
        