n = int(input())

if n == 1:
    n,m = map(int,input().split())
    print(0)
else:
    x = []
    y = []
    for _ in range(n):
        n,m = map(int,input().split())
        x.append(n)
        y.append(m)
    
    print((max(x)-min(x))*(max(y)-min(y)))