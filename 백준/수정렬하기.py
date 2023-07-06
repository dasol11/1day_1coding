n= int(input())
stk = []
for _ in range(n):
    stk.append(int(input()))
stk.sort()
stk = list(set(stk))

for i in stk:
    print(i)