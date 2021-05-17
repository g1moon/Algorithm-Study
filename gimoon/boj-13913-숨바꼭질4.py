'''
수빈이는 동생과 숨바꼭질
- x-1, x+1, 2*x
'''

#
from collections import deque
import sys
sys.setrecursionlimit(200000)

def go(n, m):
    if n != m:
        go(n, fro[m])
    print(m, end=' ')


#------------------------------------
ck = [False] * 100001
dist = [False] * 100001
fro = [False] * 100001

n,m = map(int, input().split())
q = deque()
q.append(n)
dist[n]= 0
ck[n] = True

while q:
    now = q.popleft()
    
    if (0<= now-1 <=100000) and (not ck[now-1]):
            
        dist[now-1] = dist[now] + 1
        ck[now-1] = True
        fro[now-1] = now
        q.append(now-1)
    
    if (0<= now+1 <=100000) and (not ck[now+1]):
        
        dist[now+1] = dist[now] + 1
        ck[now+1] = True
        fro[now+1] = now
        q.append(now+1)
        
    if (0<= 2*now <=100000) and (not ck[now*2]):

        dist[now*2] = dist[now] + 1
        ck[now*2] = True
        fro[now*2] = now
        q.append(now*2)
        
print(dist[m])
go(n, m)
