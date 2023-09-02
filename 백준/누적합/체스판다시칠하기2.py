import sys
input = sys.stdin.readline


def sol (c):
    
    dp = [[0]*(M+1) for _ in range(N+1)]
    for  i in range(N):
        for j in range(M):
            if (i+j) %2 == 0:
                value = board[i][j] != c
            else:
                value = board[i][j] == c
            dp[i+1][j+1] = dp[i][j+1] + dp[i+1][j] -dp[i][j] + value
            
    count = sys.maxsize
    for i in range(1, N-K +2):
        for j in range(1,M-K+2):
            count = min(count , dp[i+K-1][j+K-1]-dp[i+K-1][j-1]- dp[i - 1][j + K - 1] + dp[i - 1][j - 1])
    return count


N, M, K = map(int, input().split())

board = [list(input()) for _ in range(N)]

print(min(sol('B'), sol('W')))
