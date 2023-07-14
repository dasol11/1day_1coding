import sys

input = sys.stdin.readline

T = int(input())

stack = []
answer =[]
n = 1

for _ in range(T):
    num = int(input())
    
    while n <= num:
        stack.append(n)
        answer.append("+")
        n+=1
        
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
        
    else:
        print("NO")
        break
    
else:
    for i in answer:
        print(i)