n = int(input())
answer = 0
for i in range(n):
    s = i
    for j in str(i):
        s+= int(j)
        
    if s == n:
        answer = i
        break
print(answer)