stk = []
for _ in range(5):
    stk.append(int(input()))
stk.sort()

print(int(sum(stk)/5))
print(stk[2])