
from collections import deque

n, m = map(int, input().split())
adjLst = [[] for _ in range(n+1)]
ckLst = [-1] * (n+1)
ans = 0 
for _ in range(m):
    a, b = map(int, input().split())
    adjLst[a].append(b)
    adjLst[b].append(a)
    
for i in range(1, n+1):
    #방문했던 곳이면 넘어가고 
    if ckLst[i] == True:
        continue
    
    q = deque()
    q.append(i)
    ckLst[i] == True
    
    while q:
        cur = q.popleft()
        
        for adj in adjLst[cur]:
            if ckLst[adj] == True:
                continue
            
            q.append(adj)
            ckLst[adj] = True
            
    ans += 1
    
print(ans)    
        
