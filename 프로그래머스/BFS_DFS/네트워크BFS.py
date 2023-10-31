from collections import deque

def BFS(n, computers, com, visited):
    visited[com] = True
    que = deque()
    que.append(com)
    
    while len(que)> 0:
        com = que.pop()
        visited[com] = True
        
        for j in range(n):
            if visited[j] == False and computers[j][com] == 1 and j != com:
                que.append(j)    
    
            



def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for com in range(n):
        if visited[com] == False:
            BFS(n, computers, com, visited)
            answer += 1
        
    return answer


print(solution(4, [[1, 1, 0, 0], [1, 1,0, 0], [0, 0, 1,0],[0,0,0,1]]))