# https://www.acmicpc.net/problem/1107
# boj 1107 S1 친구 
# <메모리 : 126060, 시간 : 168 >

import sys
input = sys.stdin.readline
'''
- n*m 개에서 최대 4개 선택 -> 완탐으로 가능 
- 조합을 찾아보고 -> 그것들의 인접여부 파악 
'''
n, m, k = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))
ck = [[False]*m for _ in range(n)]
res = -1 * float('inf')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(cnt, total, curX, curY):
    global res
    
    if cnt == k:
        res = max(res, total)
        return 
    
    for x in range(curX, n):
        
        if x == curX:
            yStart = curY
        else:
            yStart = 0
            
        for y in range(yStart, m):
            if ck[x][y]:
                continue 
            flag = True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if ck[nx][ny]:
                        flag = False 
                        
            if flag:
                ck[x][y] = True
                dfs(cnt+1, total + mat[x][y], x, y)
                ck[x][y] = False
                
dfs(0, 0,0 ,0)
print(res)
