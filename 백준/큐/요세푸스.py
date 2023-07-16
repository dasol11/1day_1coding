import sys
import collections
input = sys.stdin.readline


N, K = map(int, input().split())

que = collections.deque()
for i in range(1,N+1):
    que.append(i)

answer = []

while que:
    que.rotate(-(K-1))
    answer.append(que.popleft())
    

print("<",end="")
for i in range(len(answer)):
    if (i+1) == len(answer):
        print("{}".format(answer[i]),end="")
    else:
        print("{}, ".format(answer[i]),end="")
print(">")