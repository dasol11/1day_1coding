import sys

input = sys.stdin.readline
n, m =map(int,input().split())
dic = {}
reversed_dic= {}
for i in range(n):
    s = input().strip()
    dic[s] = i+1
    reversed_dic[i+1] =  s 
    

for j in range(m):
    s = input().strip()
    if s.isdigit():
        print(reversed_dic[int(s)])
    else:
        print(dic[s])
        
        
        
import sys

input = sys.stdin.readline
n, m =map(int,input().split())
dic = {}

for i in range(n):
    s = input().strip()
    dic[s] = i+1


for j in range(m):
    s = input().strip()
    if s.isdigit():
        print(reversed_dic[int(s)])
    else:
        print(dic[s])
        
        