stk = list(map(int, input().split()))
stk.sort()

if (stk[0]+ stk[1])  > stk[2]:
    print(sum(stk))
else:
    print((stk[0]+ stk[1])*2-1)