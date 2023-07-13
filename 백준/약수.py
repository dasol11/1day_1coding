n = int(input())
stk = list(map(int,input().split()))
stk.sort()
print(stk[0]*stk[-1])


