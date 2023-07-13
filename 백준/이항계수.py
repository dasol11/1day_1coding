import sys

input = sys.stdin.readline


t = int(input())

for _ in range(t):
        
    n , m = map(int, input().split()) 


    a  = 1
    b = 1
    c = 1
    
    for i in range(1, m+1):
        a *= i
    for j in range(1, m-n+1):
        b *= j
    for k in range(1, n+1):
        c *= k

    print(a//(b*c))