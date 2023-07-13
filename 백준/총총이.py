
import sys

input = sys.stdin.readline

t = int(input())
dic = {}
for _ in range(t):
    a, b = input().split()
    if a == "ChongChong" or b == "ChongChong":
        dic[a] = 0 
        dic[b] = 0
    else:
        if a in dic or b in dic:
            dic[a] = 0 
            dic[b] = 0
            
print(len(dic))