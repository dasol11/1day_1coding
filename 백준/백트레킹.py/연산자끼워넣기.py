import sys
input = sys.stdin.readline

from collections import deque
from itertools import permutations

N = int(input())

stk = list(map(int,input().split()))
operator = ["+","-","*","//"]

op_input = list(map(int, input().split()))
op_list = [operator[i] for i in range(4) for j in range(op_input[i])]


q = deque(list(permutations(op_list, len(op_list))))
result = []

while q:
    now_list = q.popleft()
    now_sum = stk[0]
    for i in range(len(now_list)):
        if now_list[i] == "+":
            now_sum += stk[i+1]
        elif now_list[i] == "-":
            now_sum -= stk[i+1]
        elif now_list[i] == "*":
            now_sum *= stk[i+1]
        else:
            if now_sum < 0:
                now_sum = -(abs(now_sum)//stk[i+1])
            else:
                now_sum = now_sum // stk[i+1]
    result.append(now_sum)
        
print(max(result))
print(min(result))
