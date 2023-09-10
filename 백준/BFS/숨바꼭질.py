import sys
from collections import deque

input = sys.stdin.readline


N, K = map(int, input().split())

MAX = 100000
dist = [0] * (MAX +1)

que = deque()
que.append(N)

while True:
    x = que.popleft()
    
    if x == K:
        print(dist[x])
        break
    for nx in (x-1,x+1,x*2):
        if 0 <= nx <= MAX and not dist[nx]:
            dist[nx] = dist[x]+1
            que.append(nx)
            


    
