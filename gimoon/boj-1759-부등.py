# https://www.acmicpc.net/problem/1759
# boj 2529 S2 부등호 
#<메모리 : 127492, 시간 : 192>
import sys
input = sys.stdin.readline
'''
# -----솔루션--------------------------
- 1. ck 함수 내 조건 만족하고 
- 2. used에 없으면 
'''

def ck(num1, num2,opt):
    if opt == '<':
        if num1 < num2:
            return True
        return False
    
    elif opt == '>':
        if num1 > num2:
            return True
        return False


#range(1,9)중 -> 1. ck만족하고 , 2. used에 없으면 
def dfs(idx, used):
    global minNum, maxNum
    
    if idx == k+1:
        ans.append(used)
        return 
    
    #맨처음에는 다 확인
    if idx == 0:
        for i in range(10):
            dfs(idx+1, used+[i])
    else:  
        for i in range(10):
            if (i not in used)  and ck(used[idx-1], i, op[idx-1]):
                dfs(idx+1, used + [i])
    return 

    

k = int(input())
op = input().split()
minNum, maxNum = 2300000, -2300000
ans = []
dfs(0, [])
ans.sort
print(''.join(list(map(str,ans[-1]))))
print(''.join(list(map(str,ans[0]))))