# boj 1149 (S1) - RGB거리
import sys
input = sys.stdin.readline
'''
- dp[i][col] : i번째 집을 col(1,2,3)으로 칠했을 때 최솟값
- 첫번쨰 집이 R, G, B인 경우를 생각해본다
- 두번쨰 집이 1이면 이전 집은 2, 3중 작은 값 
'''
n = int(input())
mat = [[0,0,0]]
mat += [list(map(int,input().split())) for _ in range(n)]
dp = [[0,0,0] for _ in range(n+1)]

for i in range(1, n+1):
    #i를 0번색으로 칠하는 것은 -> 이전 집을 1번색과 2번색중 더 저렴한 가격의 색으로 칠하고
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + mat[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + mat[i][1]
    dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + mat[i][2]

#이렇게해서 마지막집이 0일때, 1일때, 2일때 중 -> 가장 저렴한 거 
print(min(dp[n]))




# #idx번째 집을 칠하자
# def dfs(idx, prevCol, totalPrice):
#     global ans
#     if ans <= totalPrice:
#         return 
    
#     if idx == n+1:
#         ans = min(ans, totalPrice)
#         return 
        
#     if prevCol == None:
#         for col in range(3):#rgb
#             dfs(idx+1, col, mat[idx][col])
            
#     else:
#         for col in range(3):
#             if col == prevCol:
#                 continue
#             dfs(idx+1, col, totalPrice + mat[idx][col])
    
# dfs(1, None, 0)
# print(ans)
    
    