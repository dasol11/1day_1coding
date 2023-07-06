stk=[int(i) for i in input()]
stk.sort(reverse= True)
s = ""
for i in stk:
    s += str(i)

print(s)