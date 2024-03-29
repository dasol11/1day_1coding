import sys
input = sys.stdin.readline


word1 = input().rstrip()
word2 = input().rstrip()
N = len(word1)
M = len(word2)

dp = [[0]*(M+1) for _ in range(N+1)]


for i in range(1, N+1):
    for j in range(1, M+1):
        if word1[i-1] == word2[j-1] :
            dp[i][j] = dp[i-1][j-1] +1
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[-1][-1])