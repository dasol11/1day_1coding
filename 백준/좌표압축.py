# 시간초과
# n = int(input())
# stk = list(map(int, input().split()))

# sort_stk = sorted(list(set(stk)))

# for i in stk:
#     print(sort_stk.index(i), end= " ")

import sys
input = sys.stdin.readline
n = int(input())
stk = list(map(int, input().split()))
sort_stk = sorted(list(set(stk)))

dic= {sort_stk[i]: i  for i in range(len(sort_stk))}

for i in stk:
    print(dic[i],end=" ")