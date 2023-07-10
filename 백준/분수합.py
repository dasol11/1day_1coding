import sys

input = sys.stdin.readline

def gcd (a,b):
    if a % b ==0:
        return b
    else:
        return gcd(b, a%b) 
    
a, b =map(int,input().split())

c, d =map(int,input().split())
u = a*d+c*b
bo = d*b
print(int(u/gcd(u,bo)),end=" ")
print(int(bo/gcd(u,bo)))