# boj 15990 (S3) - 1, 2, 3 더하기 5
import sys
input = sys.stdin.readline
'''
- 마지막에 1 더한 거에는 1 못 더해 
'''
import sys
input = sys.stdin.readline

dp = [ 0 for _ in range(100001)]

dp[0] = [0,0,0]#+1, +2, +3 
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4, 100001):
    tmp = [0,0,0]
    tmp[0] = (dp[i-1][1] + dp[i-1][2])%1000000009
    tmp[1] = (dp[i-2][0] + dp[i-2][2])%1000000009
    tmp[2] = (dp[i-3][0] + dp[i-3][1])%1000000009
    
    dp[i] = tmp 
    
t = int(input())
for _ in range(t):
    n = int(input())
    print(sum(dp[n])%1000000009)
    
            
            
            
