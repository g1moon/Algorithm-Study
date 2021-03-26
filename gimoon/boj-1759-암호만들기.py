# https://www.acmicpc.net/problem/15661
# boj 15661 S1 링크와스타트 
#<메모리 : 129260, 시간 : 1276>
import sys
input = sys.stdin.readline
'''
- 암호는 서로 다른 (L개의 알파벳 소문자)
- 최소 모음 1개 (a, e, i, o, u) ,
  최소 자음 2개 
- 알파벳은 오름 차순 
- 암호 사용했을 법한 문자 종류는 (C개)
- (C개의 문자들이 주어졌을 때 ) -> 가능성 있는 모든 암호 구하기 
'''

l,c = map(int, input().split()) #3 ~ 15
lst = list(map(str, input().split()))
lst.sort()
print(lst)
ans = [False] * l
ck = [False] * c 
#모음자음체크
ckVowel, ckCons = 0, 0

def dfs(idx):
    global ckVowel, ckCons
    
    if idx == l:
        if ckVowel >= 1 and ckCons >= 2: 
            print(''.join(ans))
        return 
    
    for i in range(len(lst)):
        #체크된거면 넘어가구 
        if ck[i]:
            continue
        
        #자리 수 모자르면 넘어가구
        if c-i < l - idx:
            break 
        
        #맨 처음이 아닐떄 -> 그 다음 수가 더 크다면 
        if idx != 0 and ans[idx-1] > lst[i]:
            continue 
        
        #넣을 수 있으면 넣고 
        ans[idx] = lst[i]
        ck[i] = True
        #넣은게 자음진지 모음인지 체크
        if lst[i] in ['a','e','i','o','u']:
            ckVowel += 1
        else:
            ckCons += 1
            
        dfs(idx+1)
        #빼는게 자음인지 모음인지 
        if lst[i] in ['a','e','i','o','u']:
            ckVowel -= 1
        else:
            ckCons -= 1
        
        ans[idx] = False
        ck[i] = False

dfs(0)