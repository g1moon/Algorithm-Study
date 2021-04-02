#https://www.acmicpc.net/problem/1182
#boj 1182(S2) 부분수열의 합
#<메모리 : 124984, 시간 : 268>
import sys
input = sys.stdin.readline
'''
- 인덱스별로 하나하나 보면서 더하거나 말거나 2가지 경우 모두 고려 
- target이 0이면 아무것도 더하지 않은 것도 카운트 될 수 있으므로 -> 
    target이 0이라면 ans값을 -1 해서 출력 
'''

n, target = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

def dfs(idx, total):
    global ans
    
    if idx == n:
        if target == total:
            ans += 1
        return
    
    dfs(idx+1, total + lst[idx])
    dfs(idx+1, total)

dfs(0, 0)

if target == 0:
    print(ans-1)
else:
    print(ans)
