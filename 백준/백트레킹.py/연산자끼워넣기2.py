import sys
input = sys.stdin.readline


# 6
# 1 2 3 4 5 6
# 2 1 1 1
N = int(input())
num = list(map(int, input().split()))
opr = list(map(int, input().split()))

max_val = -1e9
min_val = 1e9

def dfs (depth, total, plus, minus, mul, div):
    global max_val, min_val
    
    
    if N == depth :
        max_val = max(total, max_val)
        min_val = min(total, min_val)
        return
    else:
        if plus:
            dfs(depth +1, total + num[depth], plus-1, minus, mul, div)
        if minus:
            dfs(depth +1, total - num[depth], plus, minus-1, mul, div)
        if mul:
            dfs(depth +1, total * num[depth], plus, minus, mul-1, div)
        if div:
            dfs(depth +1, int(total / num[depth]), plus, minus, mul, div-1)


dfs(1, num[0], opr[0],opr[1],opr[2],opr[3])
print(max_val)
print(min_val)
