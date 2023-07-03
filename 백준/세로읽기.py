stk = []

for _ in range(5):
    word = input()
    li = []
    for w in word:
        li.append(w)
    stk.append(li)

s = ""
for i in range(15):
    for j in range(5):
        try:
            s += stk[j][i]
        except:
            continue
print(s)