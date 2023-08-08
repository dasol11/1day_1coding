import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

que = deque([val for idx, val in enumerate(B) if A[idx] == 0])

M = int(input())

C =  list(map(int, input().split()))


for j in C:
    que.appendleft(j)
    print(que.pop(), end= " ")
    