n = int(input())
m = int(input())
stk = []
for i in range(n,m+1):
    s = 0
    for j in range(1,i+1):
        if i%j==0:
            s +=1
    if s == 2:
        stk.append(i)
print(sum(stk))
print(min(stk))