n,m = map(int,input().split())
stk = []
for i in range(1, n+1):
    if n % i ==0:
        stk.append(i)

if len(stk) >= m:
    print(stk[m-1])
else:
    print("0")    