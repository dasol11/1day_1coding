stk = [1,1,2,2,2,8]
li = list(map(int,input().split()))

for i, j in zip(stk, li):
    print(i-j,end="")