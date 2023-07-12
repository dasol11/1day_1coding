import sys

input = sys.stdin.readline

def is_prime(x):
    if x < 2:
        return False
    for i in range(2 , int(x**0.5) +1):
        if x % i ==0:
            return False
    return True
    
n = int(input())

for _ in range(n):
    pn = int(input())
    while True:
        
        if is_prime(pn):
            print(pn)
            break
        else:
            pn += 1        
        
        
            