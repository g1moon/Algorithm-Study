import copy 
'''
- 두 팀으로 나누고 
- 같은 곳을 다른 순서로 방문 -> 먼저 순회를 마치면 승리 
- 방문할 곳의 2차원 좌표 값을 구하고 -> 각 장소를 이진트리의 노드가 되도록 구성하고 
    -> 순회 방법을 힌트로 줘 -> 각 팀이 스스로 경로 찾게 

- 서로 다른 x값
- 같은 레벨에 있는 노드는 같은 y좌표 
- 자식은 항상 y값이 작아 
- 같은 레벨에서 x값은 오름차순
- 
'''
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
result = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

def solution(nodeinfo):
    #dic{id : [x, y, l, r]}
    dic = {}
    ans = [[]]
    
    #id 넣어주기 
    for i in range(1, len(nodeinfo)+1):
        x, y = nodeinfo[i-1] 
        nodeinfo[i-1].append(i)
        dic[i] = [x,y,False, False]

    #nodeinfo = [[x,y,id], ...]
    nodeinfo = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    
    #root노드 id
    rootId = nodeinfo[0][2]
    
    #inNode : 넣어줄노드
    for inNode in nodeinfo[1:]:
        inNodeX, inNodeY, inNodeId = inNode
        comNodeId = rootId            
        
        #루트부터 비교하는 루프 
        while True:
            #처음은 루트 
            comNodeX, comNodeY, comNodeL, comNodeR = dic[comNodeId]
            
            if comNodeX > inNodeX:
                if comNodeL == False:
                    dic[comNodeId][2] = inNodeId
                    break 
                
                else:
                    comNodeId = copy.deepcopy(comNodeL)
                    continue
                    
            else:
                if comNodeR == False:
                    dic[comNodeId][3] = inNodeId
                    break 
                else:
                    comNodeId = copy.deepcopy(comNodeR)
                    continue
                    
    print(dic)

    return ans
print(solution(nodeinfo))

        
        
        
    
