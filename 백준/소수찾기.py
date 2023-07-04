n =int(input())

stk = list(map(int, input().split()))
num = 0
for i in stk:
    li = []
    if i >= 2:
        for j in range(1,i+1):
            if i % j ==0:
                li.append(j)
    if len(li) ==2 :
        num += 1
print(num)
        
            