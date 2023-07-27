import sys
input = sys.stdin.readline


n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

visited = [False for _ in range(n)]
min_val = sys.maxsize

def dfs(depth, idx):
    global min_val
    if depth == n//2 :
        sum1, sum2 = 0,0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    sum1 += graph[i][j]
                elif not visited[i] and not visited[j]:
                    sum2 += graph[i][j]
        min_val= min(min_val, abs(sum1-sum2))
        
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth + 1, i+1)
            visited[i] = False

dfs(0,0)
print(min_val)