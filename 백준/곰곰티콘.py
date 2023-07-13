
import sys

input = sys.stdin.readline

t = int(input())
num = 0
dic = {}
for _ in range(t):
    st = input().strip()
    if st == "ENTER":
        num += len(dic)
        dic = {}
    else:
        dic[st] = 0
num += len(dic)
print(num)        

                