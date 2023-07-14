import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    st = input()
    stk = []
    for i in st:
        if i == "(":
            stk.append(i)
        elif i == ")":
            if stk:
                stk.pop()
            else:
                print("NO")
                break
    else:
        if not stk:
            print("YES")
        else:
            print("NO")
        