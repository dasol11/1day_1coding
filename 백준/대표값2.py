stk = []
for _ in range(5):
    stk.append(int(input()))
stk.sort()

print(sum(stk)/5)
print(stk[2])