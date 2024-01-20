import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int,input().split())


def BFS():
    que = deque([N])
    graph = [-1] * 100001
    graph[N] = 0
    
    
    while True:
        x = que.popleft()
        
        if x == K :
            print(graph[x])
            break
        
        for nx in (x-1 , x+1, x*2):
            if 0 <= nx <= 100000 and graph[nx] == -1:
                    
                if x*2 == nx:
                    graph[nx] = graph[x]
                    que.appendleft(nx)
                    
                else:
                    graph[nx] = graph[x]+1
                    que.append(nx)

BFS()