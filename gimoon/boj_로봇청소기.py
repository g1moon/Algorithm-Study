'''
- n*m 
- 벽 or 빈칸 
- 청소기 방향(동서남북)
- r은 행, c는 열

- 현재 위치 청소
- 현재 방향을 기준으로 -> 왼쪽방향부터 탐색 ->
    - 만약 청소X -> 그 방향으로 회전하고 -> 한 칸을 전진하고 다시 1로(청소)
    - 탐색해서 청소 할 곳 없으면 -> 
'''

n, m = map(int ,input().split())
x, y, d = map(int, input().split()) #0123 -> 북동남서 
mat = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def ckAround(x,y):
    #청소할 곳이 있으면 True, 없으면 Flase
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]        

        try:
            mat[nx][ny]
            if mat[nx][ny] == 0:
                return True 
        except: pass
    return False
    
def ckLeft(x,y,d):
    #현재 위치에서 왼쪽에 0이 있는지 체크한다 
    #북동남서 
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    if d-1 == -1: i=3
    else: i = d-1
    
    nx, ny = x+dx[i], y+dy[i]
    
    try:
        mat[nx][ny]
        if mat[nx][ny] == 0:
            return True     
        else:
            return False               
    except:
        return False
    
    return False
    

def turnLeft(d):
    #d를 받아서 돌아간 d를 리턴한다 
    if d-1 == -1:
        return 3
    return d-1
        
        
def go(x,y,d,type):
    #x,y,d를 받아서 그 방향으로 한칸 전진한 x,y를 리턴
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    if type == 'st':
        return x+dx[d], y+dy[d], d
    else:
        return x-dx[d], y-dy[d], d


        
def ckBack(x,y,d):
    #후진 할 수 있으면 True
    #없으면 False
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    nx, ny = x-dx[d], y-dy[d]
    try:
        mat[x][y] #가능한 인덱스이고, 벽이 있으면 -> 불가능
        if mat[x][y] == 1:
            return False
        else: #가능한 인덱스이고 -> 벽이 아니면 
            return True
    #불가능한 인덱스면 -> False
    except:
        return False


while True:
    #1
    if mat[x][y] == 0:
        ans+=1 
        mat[x][y] = 2
    
    #만약 4방향에 청소 할 곳이 없으면
    if ckAround(x,y) == False:
        #바로 뒤로 갈 수 없다면 종료 
        if ckBack(x,y,d) == False:
            break 
        #뒤로 갈 수 있다면?
        x, y, d = go(x, y, d, 'back')
        continue 
    
    #4방향중에 어디 하나라도 청소 할 곳이 있으면?
        
    else:
        #바로 왼쪽이 청소 가능하면 -> 돌고 -> 앞으로 
        if ckLeft(x,y,d):
            d = turnLeft(d)
            x, y, d = go(x, y, d, 'st')
            continue
        #바로 왼쪽이 안되면 -> 돌기만
        else:
            d = turnLeft(d)
            continue 
        
print(mat)
print(ans)

    
    
     
    

    
    

    
