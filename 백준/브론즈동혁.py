n = int(input())

for _ in range(n):
    num = int(input())
    stk = []
    for i in [25, 10, 5, 1]:
        stk.append(str(num//i))
        num = num%i
    print(" ".join(stk))