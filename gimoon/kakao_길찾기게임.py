import copy 
import sys
sys.setrecursionlimit(10**6) #설정해주지 않으면 런타임 에러가 난다.

'''
- 넣을때 루트 노드부터 비교하면서 x값이 작으면 -> 왼쪽, 크면-> 오른쪽
- False(비어있으면) -> 넣어주고, False가 아니면(값이 있으면) -> 
    -> 그 값이 비교 대상이 된다. 
    -> 위 작업을 루프 돌리고 -> 넣어주면 종료
'''

def firDfs(nodeId):
    if dic[nodeId][2]:
        _id = dic[nodeId][2]
        firDfs(_id)
        
    if dic[nodeId][3]:
        _id = dic[nodeId][3]
        firDfs(_id)
    
    lst1.append(nodeId) 
    return 
        
def secDfs(nodeId):
    
    if nodeId not in lst2:
        lst2.append(nodeId)
        
    if dic[nodeId][2]:
        _id = dic[nodeId][2]
        secDfs(_id)
        
    if dic[nodeId][3]:
        _id = dic[nodeId][3]
        secDfs(_id)
        
    return     

def solution(nodeinfo):
    global dic, lst1, lst2
    lst1, lst2 = [], []
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
                    
    #여기까지 오면 dic만들어짐-------------
    firDfs(rootId)
    secDfs(rootId)
    ans = [lst2, lst1]
    
    return ans