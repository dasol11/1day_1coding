import sys

input = sys.stdin.readline

n = int(input())
dic = {}
for _ in range(n):
    name, state = map(str,input().split())
    if state == "enter":
        dic[name] = state
    else:
        del dic[name]
skt = sorted(dic ,reverse=True)

for i in skt:
    print(i)
    