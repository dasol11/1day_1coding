n = int(input())
stk = []
for _ in range(n):
    stk.append(list(map(int, input().split())))
stk.sort( key=lambda x:(x[1],x[0]))
print("==========")
for i in stk:
    print(i[0],i[1])
    