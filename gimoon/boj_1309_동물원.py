import sys
input = sys.stdin.readline

#우리의 크기 : N*2 
n = int(input())
dp = [[1]*3 for _ in range(n+2)]

for i in range(2, n+2):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2])%9901
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2])%9901
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1])%9901
    
print(dp[n+1][0])
    