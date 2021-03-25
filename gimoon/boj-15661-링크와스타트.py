# https://www.acmicpc.net/problem/15661
# boj 15661 S1 링크와스타트 
#<메모리 : 129260, 시간 : 1276>
import sys
input = sys.stdin.readline
'''
- 그냥 링크팀 스타트팀으로 나누어지는 모든 경우 구해서 -> 차이 구하기..
- 무식하게 풀었는데 n의 수가 크지 않아서 시도했습니다. 
'''

n = int(input())
mat = [ list(map(int, input().split())) for _ in range(n)]
ans = float('inf')
cnt = 0

def calSumOfList(lst):
    global cnt
    ret = 0 
    if len(lst) == 1:
        return 0

    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            ret += mat[lst[i]][lst[j]]
            ret += mat[lst[j]][lst[i]]
            
    return ret             

def dfs(idx,start, link):
    global ans 
    if idx == n:
        if not start or not link:
            return 
        
        sumOfStart = calSumOfList(start)
        sumOfLink = calSumOfList(link)
        
        gap = abs(sumOfStart - sumOfLink)
        ans = min(ans, gap)
        return 
    
    newStart = start + [idx] 
    newLink = link + [idx]
    
    dfs(idx+1, newStart, link)
    dfs(idx+1, start, newLink)
    
dfs(0, [], [])
print(ans)
