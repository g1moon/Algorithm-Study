# https://www.acmicpc.net/problem/1759
# boj 1759 G5 암호만들기 
#<메모리 : 123688, 시간 : 140>
import sys
input = sys.stdin.readline
'''
# -----솔루션--------------------------
- 오름차순이니 리스트를 오름차순 정렬하고 
- 조건1 : 체크된거면 넘어가구 
  조건2 : 자리 수 모자르면 넘어가구 
  조건3 : 맨 처음이 아닌경우에 -> 그 다음 수가 마지막에 추가한 것 보다 더 크다면 넘어가 
  조건4 : 자음 모음 개수 맞아야 한다.
- 위 조건을 벗어나지 않는 모든 경우 출력   

# -----문제요약-------------------------
- 암호는 서로 다른 (L개의 알파벳 소문자)
- 최소 모음 1개 (a, e, i, o, u) 
  최소 자음 2개 
- 알파벳은 오름 차순 
- 암호 사용했을 법한 문자 종류는 (C개)
- (C개의 문자들이 주어졌을 때 ) -> 가능성 있는 모든 암호 구하기 
'''

l,c = map(int, input().split()) #3 ~ 15
lst = list(map(str, input().split()))
lst.sort()
# print(lst)
ans = [False] * l
ck = [False] * c 
#모음자음개수체크
countVowel, countCons = 0, 0
        
def dfs(idx):    
    global countVowel, countCons

    if idx == l:
        #조건 4: 자음 모음 개수 맞아야 한다.
        if countVowel >= 1 and countCons >= 2: 
            print(''.join(ans))
        return 
    
    for i in range(len(lst)):
        #조건1 : 체크된거면 넘어가구 
        if ck[i]:
            continue
        
        #조건2 : 자리 수 모자르면 넘어가구
        if c-i < l - idx:
            break 
        
        #조건3 : 맨 처음이 아닌경우에 -> 그 다음 수가 마지막에 추가한 것 보다 더 크다면 넘어가 
        if idx != 0 and ans[idx-1] > lst[i]:
            continue 
        
        #넣을 수 있으면 넣고 
        ans[idx] = lst[i]
        ck[i] = True
        
        #넣은게 자음진지 모음인지 체크
        if lst[i] in ['a','e','i','o','u']:
            countVowel += 1
        else:
            countCons += 1
        
        #다음 인덱스로 넘어가 
        dfs(idx+1)
        
        #빼는게 자음인지 모음인지 체크 
        if lst[i] in ['a','e','i','o','u']:
            countVowel -= 1
        else:
            countCons -= 1

        ans[idx] = False
        ck[i] = False

dfs(0)

