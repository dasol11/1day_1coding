import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

visit =[False for _ in range(n)]
min_val = sys.maxsize

def backTracking(depth, idx):
    global min_val
    
    if depth == n//2:
        sum1, sum2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visit[i] and visit[j]:
                    sum1 += graph[i][j]
                elif not visit[i] and not visit[j]:
                    sum2 += graph[i][j]
        min_val = min(min_val,abs(sum1-sum2))
        return           
                    
        
    for i in range(idx,n):
        if not visit[i]:
            visit[i] = True
            print(depth+1, i+1)
            backTracking(depth+1, i+1)
            visit[i] = False
        
    
backTracking(0, 0)