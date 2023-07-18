
import sys
import collections
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    
    N, M = map(int, input().split())
    que = collections.deque((map(int,(input().split()))))
    taget = que[M]
    num = 0
    while que:
        M -= 1
        best = max(que)
        frt = que.popleft()
        
            
        if frt == best:
            num += 1
            if M < 0:
                print(num)
                break
        
        else:
            que.append(frt)
            if M < 0:
                M = len(que) -1
    
        
                    