x = []
y = []
answer = []
for _ in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
    

for i in x:
    if x.count(i) == 1:
        answer.append(str(i))
        break
for j in y:
    if y.count(j) == 1:
        answer.append(str(j))
        break
print(" ".join(answer))        