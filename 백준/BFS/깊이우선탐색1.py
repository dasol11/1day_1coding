import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(idx):
    global cnt
    visited[idx] = cnt
    for val in graph[idx]:
        if visited[val] == 0:
            cnt += 1
            visited[val] = cnt
            dfs(val)
        
N, M, R = map(int,input().split())

visited = [0 for _ in range(N+1)]

graph = [[] for _ in range(N+1)]

cnt = 1
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()

dfs(R)

for i in range(1, N+1):
    print(visited[i])
