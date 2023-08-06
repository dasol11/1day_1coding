import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

que = deque([(rota, idx +1) for idx, rota in enumerate(arr)])

answer = []
while que:
    rota, idx = que.popleft()
    answer.append(str(idx))
    if rota > 0:
        que.rotate(1-rota)
    else:
        que.rotate(-rota)
    
print(" ".join(answer))