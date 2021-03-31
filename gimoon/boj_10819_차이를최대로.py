# https://www.acmicpc.net/problem/10819
# boj 10819 S2 차이를 최대로 
# <메모리 : 125128, 시간 : 176 >

'''
- dfs로 모든 경우의 인덱스 리스트(?)를 구하고 -> 그 결과를 계산해 최댓값을 찾는다.
'''
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))


ck = [False] * n
res = [False] * n
ans = 0

def dfs(idx):
    global ck, res, ans
    
    if idx == n:
        ans = max(ans, sumNewLst(res))
        return 
    
    for i in range(n):
        if not ck[i]:
            res[idx] = i
            ck[i] = True
            dfs(idx+1) 
            ck[i] = False

def sumNewLst(lst):
    ret = 0 
    for i in range(0, len(lst)-1):
        idx1, idx2 = lst[i], lst[i+1]
        ret += abs(a[idx1] - a[idx2])
    return ret
                    
dfs(0)
print(ans)



    
    