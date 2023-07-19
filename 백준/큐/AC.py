import sys
from collections import deque

import ast

input = sys.stdin.readline


T = int(input())
for _ in range(T):
        
    p = input()

    n = int(input())

    string = input()
    que = deque(ast.literal_eval(string))
    rev = 0
    
    for j in p:
        if j == "R":
            rev += 1
            
        elif j == "D":
            if que: 
                if rev % 2 == 0:       
                    que.popleft()
                else:
                    que.pop()
            else:
                print("error")
                break
    else:
        
        if rev % 2 != 0:
            que.reverse()
        print("["+ ",".join(map(str,que)) + "]")    
            