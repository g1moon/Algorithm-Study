import copy 
import sys
sys.setrecursionlimit(10**6) #설정해주지 않으면 런타임 에러가 난다.


def solution(stones, k):
    #최솟값 빼고 시작 
    minNum = min(stones)
    for i in range(len(stones)):
        stones[i] -= minNum

    cnt = minNum     
    outerDone = False 
    while not outerDone:
        cur = -1 
        e = len(stones)
        innerDone = False
        
        while not innerDone:
            # print(stones)
            for i in range(1, k+1):
                #만약 도착하면 -> cnt+=1해주고 종료  
                if (cur+i) == e:
                    cnt += 1
                    innerDone = True
                    break    
                #0이 아니면 -> 건너가고 -> 줄여주고 -> 
                
                #0이면 그냥 넘어가 -> 근데 0인데 k를 다 쓰면(건너 갈 수 없음) -> 모두 종료
                if (stones[cur+i]) == 0:
                    if i == k:
                        outerDone = True 
                        innerDone = True
                        break 
                    continue 
                
                #이동하고, 1씩 뺴주고 
                cur += i 
                stones[cur] -= 1
                break
            
    return cnt

'''
- 디딤돌의 숫자는 한번 밟으면 -> 1씩 줄어든다 
- 0이되면 -> 밟을 수 없음 -> 그 다음 돌로 한번에 여러칸 뛸 수 있음 
- 다음으로 밟을 수 있는 디딤돌이 여러개면 -> 가장 가까운 디딤돌로만 뛸 수 있음(?)
'''

stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
print(solution(stones, k))