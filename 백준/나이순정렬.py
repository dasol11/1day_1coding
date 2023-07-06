n = int(input())
stk = []
for _ in range(n):
    a =  input().split()
    a[0] = int(a[0])
    stk.append(a)

stk.sort(key=lambda x:x[0])

for i in stk:
    print(i[0],i[1])
