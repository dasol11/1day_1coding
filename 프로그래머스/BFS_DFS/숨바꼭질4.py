import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())
dist = [0] * (100001)
move = [0] * (100001)


def BFS():
    que = deque()
    que.append(N) 
    while que:
        x = que.popleft()
        if x == K:
            print(dist[x])
            stk = []
            temp = x
            for _ in range(dist[x]+1):
                stk. append(temp)
                temp = move[temp]
            print(" ".join(map(str, stk[::-1])))
            return (x)        
        for i in (x+1, x-1 , 2*x):
            if 0 <= i <= 100000 and  dist[i] == 0:
                que.append(i)
                dist[i] = dist[x] +1
                move[i] = x
                
                
BFS()
print(move[:20])
