n,m = map(int,input().split())
stk = list(map(int,input().split()))
answer = 0
for i in range(n-2):
    for j in range(1,n-1):
        for k in range(2,n):
            s = stk[i] + stk[j] + stk[k]
            if m >= s and (m-answer) > (m-s) and i!=j and j!=k and k!=i :
                answer = s
                print(i,j,k,s)
print(answer)           