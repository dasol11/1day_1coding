import sys
input = sys.stdin.readline



def dfs(R):
    global cnt
    visited[R] = cnt
    
    for val in graph[R]:
        if visited[val] ==0:
            cnt += 1 
            dfs(val)
    

N, M, R = map(int,input().split())
graph= [[] for _ in range(N+1)] 
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    
visited = [0] * (N+1)
cnt= 1

dfs(R)

for i in range(1, N+1):
    print(visited[i])