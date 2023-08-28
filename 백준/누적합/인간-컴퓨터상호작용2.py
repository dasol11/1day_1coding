import sys
input = sys.stdin.readline

s = input().rstrip()

dp = [[0]*26]
dp[0][ord(s[0])-97] = 1
for i in range(1, len(s)):
    dp.append(dp[-1][:])
    dp[i][ord(s[i])-97] += 1
    
for _ in range(int(input())):
    c, s, e = list(input().split())
    s, e = map(int,[s,e])
    if s == 0:
        print(dp[e][ord(c)-97])
    else:
        print(dp[e][ord(c)-97]-dp[s-1][ord(c)-97])