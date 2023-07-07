import sys

input = sys.stdin.readline

n ,m = map(int,input().split())
dic = {input(): 0 for _ in range(n)}
answer = 0
for _ in range(m):
    s = input()
    if s in dic:
        answer += 1
        
print(answer)