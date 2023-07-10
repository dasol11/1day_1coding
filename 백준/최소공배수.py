import sys

# input = sys.stdin.readline

# def gcd(x, y):  
#   if y == 0:
#     return x
#   else:
#     return gcd(y, x%y)
  
# num = int(input().strip())
# for _ in range(num):
#     n, m =map(int,input().split())
#     print((n*m)//gcd(n,m))

input = sys.stdin.readline

def gcd(x, y):  
  if x % y ==0:
      return y
  else:
      return gcd(y, x % y) 

n, m =map(int,input().split())
print((n*m)//gcd(n,m))
print(gcd(n,m))