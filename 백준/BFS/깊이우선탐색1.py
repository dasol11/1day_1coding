import sys
input = sys.stdin.readline

N, M, R = map(int,input().split())


def dfs(idx):
    global cnt
    visited[idx] = cnt
    for val in graph[idx]:
        if visited[val] == 0:
            cnt += 1
            visited[val] = cnt
        

visited = [[0] for i in range(N+1)]

graph = [[] for _ in (M+1)]
cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    
dfs(R)

for i in range(1, N+1):
    print(visited[i])
