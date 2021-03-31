# https://www.acmicpc.net/problem/1248
# boj 1248 G3 맞춰봐 
# <메모리 : 129196, 시간 744>

import sys 
input = sys.stdin.readline

def ck(idx):
    s = 0
    for i in range(idx,-1,-1):
        s += ans[i]
        
        if sign[i][idx] == '+' and s <= 0:
            return False
        if sign[i][idx] == '0' and s != 0:
            return False
        if sign[i][idx] == '-' and s >= 0:
            return False
        
    return True

def dfs(idx):
    if idx == n:
        return True
    
    if sign[idx][idx] == 0:
        ans[idx] = 0
        return ck(idx) and dfs(idx+1)

    for i in range(1, 11):
        ans[idx] = i * sign[idx][idx]
        if ck(idx) and dfs(idx+1):
            return True
        
    return False

#-----------------------------
n = int(input())
s = input()
sign = [[0]*n for _ in range(n)]
ans = [0]*n
cnt = 0

for i in range(n):
    for j in range(i,n):
        if s[cnt] == '0':
            sign[i][j] = 0
        elif s[cnt] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = -1
            
        cnt += 1

dfs(0)
print(' '.join(map(str,ans)))
