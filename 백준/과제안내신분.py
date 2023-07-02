num =[i for i in range(1,31)]

for _ in range(28):
    i = int(input())
    if i in num:
        num.remove(i)
        
for j in num:
    print(j)