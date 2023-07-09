import sys

input = sys.stdin.readline
n=input().strip()
stk = []
for i in range(len(n)):
    for j in range(len(n)):
        stk.append(n[i:i+j])

print(len(set(stk)))