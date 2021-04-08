# boj 14002 (G5) - 가장 긴 증가하는 부분 수열4
import sys
input = sys.stdin.readline
'''
- dp[idx] : lst[idx]가 마지막으로 올 때 
- 마지막 인덱스 정해주고, 0부터 마지막 인덱스 전 까지 확인하며 -> 작은 값 확인  
'''

n = int(input())
dp = [[[], 1]  for _ in range(n+1)]
lst = list(map(int, input().split()))

    
dp[0] = [[lst[0]], 1]

ansLen = 1
ansLst = [lst[0]]

for last in range(1, n):
    tmp = [lst[last]]
    m = 1
    dp[last] = [tmp, m]
    
    for i in range(0, last):
        if lst[last] > lst[i] and dp[i][1] + 1 > m:
            tmp = dp[i][0] + [lst[last]]
            m = dp[i][1] + 1
            dp[last] = [tmp, m]
        #만약 갱신된게 
        if m > ansLen:
            ansLen = m
            ansLst = dp[last][0]
            
            
print(ansLen)
print(*ansLst)
            
            
            
