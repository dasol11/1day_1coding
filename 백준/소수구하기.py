import sys

input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2 , int(x**0.5) +1):
        if x % i ==0:
            return False
    return True

s , e = map(int, input().split())

for i in range(s, e +1):
    if is_prime(i):
        print(i)
    
