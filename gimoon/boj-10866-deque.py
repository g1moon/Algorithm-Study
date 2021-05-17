'''
수빈이는 동생과 숨바꼭질
- x-1, x+1, 2*x
'''
from collections import deque
import sys
#
input = sys.stdin.readline
q = deque()
n = int(input())
s = 0
for _ in range(n):
    tmp = input().split()
    if tmp[0] == 'push_front':
        s+=1
        num = tmp[1]
        q.appendleft(num)
        
    elif tmp[0] == 'push_back':
        s+=1
        num = tmp[1]
        q.append(num)
            
    elif tmp[0] == 'pop_front':
        if q:
            s-=1
            popped = q.popleft()
            print(popped)
        else:
            print(-1)
        
    elif tmp[0]== 'pop_back':
        if q:
            s-=1
            popped = q.pop()
            print(popped)
        else:
            print(-1)
        
    elif tmp[0] == 'size':
        print(s)
        
    elif tmp[0] == 'empty':
        if s!=0:
            print(0)
        else:
            print(1)
    
    elif tmp[0] == 'front':
        if s!=0:
            print(q[0])
        else:
            print(-1)
            
    elif tmp[0] == 'back':
        if s!=0:
            print(q[-1])
        else:
            print(-1)
            
    
        
        
        
    
    
    
    
    
    
    
    
    
    
    

