total = int(input())
s = 0
for _ in range(int(input())):
    n, m = map(int, input().split())
    s += n*m
    
if total == s:
    print("Yes")
else:
    print("No") 

print(int(input())//4*"long "+"int")
print("long "*int(input())//4+"int")