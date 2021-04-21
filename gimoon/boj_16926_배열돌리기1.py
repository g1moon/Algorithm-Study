'''
- 문제를 완전 잘못 이해함 
- 새로 짜야함.. 
- 테두리 하나씩 왼쪽으로 돌려야 하는데 전체를 돌려버림.
'''
n, m, r = map(int, input().split())
mat = []

ansMat = [[False] *m for _ in range(n)]
flatList = []
ckScan = [[False] * m for _ in range(n)]
ckInput = [[False] * m for _ in range(n)]
for _ in range(n):
    mat.append(list(map(int, input().split())))

def scanAround(start, type, lst):
    flatList = []
    #오른쪽 -> 아래 -> 왼쪽 -> 위 
    nx, ny = start[0], start[1]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    if type == 'scan':
        flatList.append(mat[nx][ny])
        ckScan[nx][ny] = True
    else:
        ansMat[nx][ny] = lst.pop(0)
        ckInput[nx][ny] = True
        
    
    for i in range(4):
        while True:
            nx += dx[i]
            ny += dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                nx -= dx[i]
                ny -= dy[i]
                break 
            
            if type =='scan' and ckScan[nx][ny]:
                # print(1)
                nx -= dx[i]
                ny -= dy[i]
                break
            
            if type =='input' and ckInput[nx][ny]:
                # print(2)
                nx -= dx[i]
                ny -= dy[i]
                break
            
            if type == 'scan':
                flatList.append(mat[nx][ny])
                ckScan[nx][ny] = True

            else:
                ansMat[nx][ny] = lst.pop(0)
                ckInput[nx][ny] = True
                
    if type == 'scan':
        return flatList


#-----------------------------
start = (0,0)
while True:
    x, y = start[0], start[1]
    if ckScan[x][y] == True:
        break 
    rotatedList = []
    
    flatList = scanAround(start, 'scan', [])
    rotatedList = flatList[r%(len(flatList)):] + flatList[:r%(len(flatList))]
    scanAround(start, 'input', rotatedList)
    
    start = (x+1, y+1)
    
for line in ansMat:
    print(*line)


                
    
    


    