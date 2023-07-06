n = int(input())
stk = []
for _ in range(n):
    s = input()
    if s not in stk:
        stk.append(s)
stk.sort( key = lambda x:(len(x),x))
for i in stk:
    print(i)
    