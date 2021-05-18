'''
- n명의 사람
- 0~n-1 번 까지 
- 일부 사람들은 친구
- n(사람의 수), m(친구 관계의 수)
'''

'''
0에서 다음 거로 간다.

'''
def dfs(idx, num):
    global ans
    #if idx가 n-1이면 종료 
    if num == 4:
        ans = 1
        return 

    for adjNode in lst[idx]:
        if not ck[adjNode]:
            ck[adjNode] = True
            dfs(adjNode, num+1)
            ck[adjNode] = False 
            
if __name__ == '__main__':
    import sys 
    input = sys.stdin.readline
    res = False
    
    n, m = map(int, input().split())
    #idx번에서 -> 갈 수 있는 경우 
    lst = [ [] for _ in range(n+1)]
    ck = [False] * (n+1)
    ans = 0
    
    
    for _ in range(m):
        #a에서 b로 갈 수 있음
        a, b = map(int, input().split())
        lst[a].append(b)
        lst[b].append(a)
        

    for i in range(n):
        ck[i] = True
        res = dfs(i, 0)
        ck[i] = False
    
    if ans == 1:
        print(1)
    else:
        print(0)
    
        
    


'''
- edgeLst(간선리스트) 
    -> E라는 배열에 간선을 다 저장 E[0] = 1 2, E[1] = 1 5, E[2] = 2 3 .....
    -> 각 간선의 앞 정점을 기준으로 개수 카운트 
    -> cnt[i] = n개... -> ex) cnt[0] = 0, cnt[1] = 2 , cnt[2] = 1
    -> 그리고 이거를 앞에서 부터 누적(피보나치처럼?)
    -> 그럼 3
    
                ->  edgeLst[from].append(to)
                    edgeLst[to].append(from)
- adjMat(인접행렬)
            -> adjMat[from][to] = adjMat[to][from] = 1 
            
- adjList
            -> adjList[from].append(to)
            -> adjList[to].apend(from)
'''