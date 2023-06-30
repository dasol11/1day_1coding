n,m =map(int,input().split())

stk =[str(i+1) for i in range(n)]

for _ in range(m):
    s,e = map(int,input().split())
    stk[s-1:e] = reversed(stk[s-1:e])
    
print(" ".join(stk))  
