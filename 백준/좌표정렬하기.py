n = int(input())
stk = []
for _ in range(n):
    stk.append(list(map(int, input().split())))
stk.sort( key=lambda x:(x[0], x[1]))

for i in stk:
    print(i[0],i[1])
    