def solution(board, k):
    answer = 0
    n, m = len(board), len(board[0])
    for i in range(n):
        for j in range(m):
            if i+j <= k:
                answer += board[i][j]
    return answer



def solution(board, k):
    return sum(board[i][j] for i in range(len(board)) for j in range(len(board[0])) if i + j <= k)
