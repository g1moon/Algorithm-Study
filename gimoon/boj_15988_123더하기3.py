# boj 15988 (S2) - 1, 2, 3 더하기 3
import sys
input = sys.stdin.readline
'''
- dp[i] += (dp[i-1] + dp[i-2] + dp[i-3])%mod
'''
import sys
input = sys.stdin.readline

limit = 1000000 + 1 
mod = 1000000009

dp = [0] * 1000001
dp[0],dp[1],dp[2],dp[3] = 0,1,2,4

for i in range(4,limit):
    dp[i] += (dp[i-1] + dp[i-2] + dp[i-3])%mod
        
t = int(input())
for _ in range(t):
    n = int(input())    
    print(dp[n]%mod)
            
            
            
