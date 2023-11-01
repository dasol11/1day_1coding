

def solution(n, computers):
    visited=[False] *n
    answer = 0
    for ball in range(n):
        if visited[ball] == False:
            DFS(n, computers,visited, ball)
            answer += 1
    return answer


def DFS(n, computers,visited, ball):
    
    visited[ball] =  True
    for j in range(n):
        if ball != j and computers[j][ball] == 1 and visited[j] == False:
            DFS(n,computers,visited, j)
            
            