#------------------------------
t = int(input())
itemLst = [list(map(int, input())) for _ in range(t)]
k = int(input())

#1 시계방향 , -1은 반시계----------------------
def turnItem(item, dir):
    if dir == 1:
        ret = [item[-1]] + item[:-1]
    elif dir == -1:
        ret = item[1:] + [item[0]]

    return ret

def ck(rotatedIdx, rotatedDir, dir):
    global itemLst
    '''
    rotatedIdx : 회전한 아이템의 인덱스 
    rotatedDir : 회전한 아이템의 돌아간 방향 
    dir : 어느쪽으로 나아가면서 체크 할 것 인지
    '''
    # 만약 방향이 -1로 돌았으면 이제는 1로 돌아줘야해 
    if rotatedDir == -1:
        curDir = 1
    else:
        curDir = -1
     
    
    #맨 마지막 아이템이나 맨 처음 아이템이 회전한게 아니라면     
    if (1<= rotatedIdx <= len(itemLst)-2):
        if dir == 'L':
            if itemLst[rotatedIdx][6] != itemLst[rotatedIdx-1][2]:
                itemLst[rotatedIdx-1] = turnItem(itemLst[rotatedIdx-1], curDir)
                if rotatedIdx-1 == 0:
                    return  
                ck(rotatedIdx-1, curDir, 'L')
        
        
        #R
        else:
            if itemLst[rotatedIdx][2] != itemLst[rotatedIdx+1][6]:
                itemLst[rotatedIdx+1] = turnItem(itemLst[rotatedIdx+1], curDir)
                if rotatedIdx+1 == t-1:
                    return  
                ck(rotatedIdx+1, curDir, 'R')
        
    
    elif rotatedIdx == 0:
        if itemLst[rotatedIdx][2] != itemLst[rotatedIdx+1][6]:
            itemLst[rotatedIdx+1] = turnItem(itemLst[rotatedIdx+1], curDir)
            ck(rotatedIdx+1, curDir, 'R')
        
    
    elif rotatedIdx == t-1:
        if itemLst[rotatedIdx][6] != itemLst[rotatedIdx-1][2]:
            itemLst[rotatedIdx-1] = turnItem(itemLst[rotatedIdx-1], curDir)
            ck(rotatedIdx-1, curDir, 'L')
        
        
        
                
#————————————————————

for _ in range(k):
    a, d = map(int, input().split())
    #우선 거기거 돌려 
    itemLst[a-1] = turnItem(itemLst[a-1], d)
    if a-1 == 0:
        ck(a-1, d, 'R')
    elif a-1 == t-1:
        ck(a-1, d, 'L')
    else:
        #ck->left
        ck(a-1, d, 'L')
        #ck-right
        ck(a-1, d, 'R')
    
ans = 0
for i in range(len(itemLst)):
    if itemLst[i][0] == 1:
        ans+=1
print(ans)