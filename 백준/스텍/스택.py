import sys

input = sys.stdin.readline

T = int(input())
stack =[]
for _ in range(T):
    stk = input().split()
    if stk[0] == "push":
        stack.append(int(stk[1]))
    elif stk[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif stk[0] == "size":
        print(len(stack))
    elif stk[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif stk[0] == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)