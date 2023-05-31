def solution(n):
    if n == 1:
        answer = [0]
    else:
            
        answer = [[0 for col in range(n)] for row in range(n)]
        
        #상하좌우
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        
        direction = 0
        
        #좌표
        x = 0
        y = 0
        
        for i in range(1, n*n+1):

            answer[x][y] = i
            nx = x + dx[direction % 4]
            ny = y + dy[direction % 4]
            
            # nxn을 벗어난 경우
            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1 :
                direction += 1
                nx = x + dx[direction % 4]
                ny = y + dy[direction % 4]
            
            if answer[nx][ny] != 0:
                direction += 1
                nx = x + dx[direction % 4]
                ny = y + dy[direction % 4]
            x = nx
            y = ny
            
                    
    return answer


a = solution(1)
print(a)