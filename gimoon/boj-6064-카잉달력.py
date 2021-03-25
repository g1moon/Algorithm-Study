# https://www.acmicpc.net/problem/6065
# boj 6065 S1 카잉달력 

import sys
input = sys.stdin.readline
'''
- 브루트포스라 생각해서 진짜 무식하게 접근해봤는데 메모리 초과, 시간 초과네여...
- x,y 부분에서 1씩 빼주면 나누기 연산으로 해결 가능 (나머지 연산)
- 이렇게되면 m 단위로 y부분만 확인해주면 된다...
'''
t = int(input())
for _ in range(t):
    m,n,x,y = map(int,input().split())
    
    #뺴주면 나누기 연산으로 가능 
    x -= 1
    y -= 1
    tmp = x
    
    #m단위로 봐주면 된다. 
    while tmp < n*m:
        if tmp%n == y:
            print(tmp+1)
            break
        tmp += m
        
    else:
        print(-1)

#방법1-----------------------------------
# #input 
# t = int(input())
# lst = []
# maxM, maxN = -1, -1 
# for _ in range(t):
    
#     M, N, x, y = map(int, input().split())
#     cnt = 0
    
#     xLst = [i for i in range(1, M+1)]
#     yLst = [i for i in range(1, N+1)]
    
#     xLst = xLst * (40000//M + 40000%M)
#     yLst = yLst * (40000//N + 40000%N)
    
#     # print(len(xLst))
#     # print(len(yLst))
    
#     for i in range(len(xLst)):
#         curX, curY = xLst[i], yLst[i]
#         if curX == x and curY == y:
#             print(i+1)
#             break 
#     else:
#         print(-1)

#방법2----------------------------------
# #input 
# t = int(input())
# lst = []
# maxM, maxN = -1, -1 
# for _ in range(t):
    
#     M, N, x, y = map(int, input().split())
#     cnt = 0
    
#     curX, curY = 1, 1
#     cnt = 1
#     while True:

#         if curX == x and curY == y:
#             print(cnt)
#             break 
        
#         if curX == M and curY == N:
#             print(-1)
#             break 
        
            
        
#         if curX == M:
#             curX = 1 
#         else:
#             curX += 1
        
#         if curY == N:
#             curY = 1 
#         else:
#             curY += 1
        
#         cnt+=1
            