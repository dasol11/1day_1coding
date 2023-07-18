
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())


pos = list(map(int,input().split()))
que = deque(i for i in range(1,n+1))
count = 0

for i in pos:
    while True:
        if que[0] == i:
            que.popleft()
            break
        else:
            if que.index(i) <= len(que)//2 :
                que.rotate(-1)
                count += 1
            else:
                que.rotate(1)
                count += 1
                
print(count) 
        