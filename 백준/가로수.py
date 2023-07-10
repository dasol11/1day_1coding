import sys

input = sys.stdin.readline

def gcd (a, b):
    if a % b ==0:
        return b
    else:
        return gcd(b,a % b)
    
n = int(input().strip())
s = int(input().strip())

red = []
for _ in range(n-1):
    num = int(input().strip())
    red.append(num-s)
    s = num
    
g = red[0]
for i in range(1,len(red)):
    g = gcd(g,red[i])

answer = 0
for j in red:
    answer += j//g -1
    print(answer)    


    