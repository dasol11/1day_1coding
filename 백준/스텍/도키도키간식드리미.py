import sys

from collections import deque

input  = sys.stdin.readline

N = int(input())

que = deque(map(int, input().split()))
stk = deque()

#5
#5 3 1 2 4
idx = 1
while que:
    if que and que[0] == idx:
        que.popleft()
        idx += 1
    else:
        stk.append(que.popleft())
    while stk and stk[-1] == idx:
        stk.pop()
        idx += 1
if stk:
    print("Sad")
else:
    print("Nice")