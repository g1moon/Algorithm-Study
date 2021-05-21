'''
- 그래프의 정점의 집합을 둘로 분할 
- 각 집합에 속한 정점끼리는 서로 인접하지 ㅇ낳게 분할 할 수 있을 때 

- 그래프가 입력으로 주어지면 -> 이분 그래프인지 아닌지 판별
'''

if __name__ == '__main__':
    from collections import deque
    k = int(input())
    #첫쨰 줄에는 그래프의 정점의 개수v, 간선의 개수 e

    for _ in range(k):
        v, e = map(int ,input().split())
        colLst = [-1] *(v+1)
        adjLst = [[] for _ in range(v+1)]
        visited = []
        ans = 'YES'
        
        for _ in range(e):
            a, b = map(int, input().split())
            adjLst[a].append(b)
            adjLst[b].append(a)
        
        visited = [-1]*(v+1)
        visited[1] = True
        
        
        #모든 점에서부터 봐주기(연결노드가 아닐 수 있음)
        for i in range(1, v+1):          
            q = deque()  
            q.append(i)
            if colLst[i] != -1:
                pass
            else:
                colLst[i] = 'R'
        
            while q:
                curNode = deque.popleft(q)
                curCol = colLst[curNode]
                
                for adjNode in adjLst[curNode]:
                    adjCol = colLst[adjNode]
                    
                    #여기서 인접한 것의 색이 같으면 종료
                    if curCol == adjCol:
                        ans = 'NO'
                        break 
                    
                    if visited[adjNode] == -1:
                        q.append(adjNode)
                        visited[adjNode] = True
                        #색 반대로 칠해주기 
                        if curCol == 'R':
                            colLst[adjNode] = 'B'
                        else:
                            colLst[adjNode] = 'R'
                            
            if ans == 'NO':
                break
            else:
                continue
                
        
                        
        print(ans)
        
        
        
            
            
        
        
        
        
        
        
        
        
    
