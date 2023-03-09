def solution(board):
    answer = 0
    bom = []
    N = len(board)
    for i in range(N):
        for j in range(N):
            if board[i][j]== 1:
                bom.append((i,j))
    
    add_x = [-1,  0, 1, -1, 1, -1, 0, 1]
    add_y = [-1, -1,-1,  0, 0,  1, 1, 1]
    
    for x, y  in bom:
        for k in range(8):
            bom_x = x + add_x[k]
            bom_y = y + add_y[k]
            
            if (0 <= bom_x < N) and (0 <= bom_y < N):
                board[bom_x][bom_y] = 1
        
    for i in range(N):
        for j in range(N):
            if board[i][j]== 0:
                answer += 1
    
    return answer

a = solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]])
print (a)

b = solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]])
print (b)
c = solution([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]])
print (c)