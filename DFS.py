def dfs (graph, v, visited):
    visited[v] = True
    print(v, end = " ")
    for i in graph[v]: 
        if not visited[i]: # if not은 Ture / False 여부를 판단하는 조건문!
            dfs(graph, i , visited)
            

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]    
]

visited = [False] * 9

dfs (graph, 2,visited)