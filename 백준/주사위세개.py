stk =sorted(input().split())
c = [stk.count(i) for i in stk]
idx = c.index(max(c))
n1,n2,n3 = map(int,stk)

if n1==n2 and n2==n3:
    print(10000+n1*1000)
elif n1==n2 or n2==n3 or n1==n3:
    print(1000+int(stk[idx])*100)
else:
    print(max(n1,n2,n3)* 100)