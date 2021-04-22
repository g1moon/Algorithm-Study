#14499 주사위 굴리기 
'''
- (n * m)  r:row , c:col 
- 
'''
n, m, x, y, k = map(int, input().split())
mat = [ list(map(int, input().split())) for _ in range(n)] 
cmdList = list(map(int, input().split())) #동서북남 

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

#주사위 윗면 -> 0, 아랫면 -> 5
dice = [0,0,0,0,0,0]

for cmd in cmdList:
    nx, ny = x + dx[cmd], y + dy[cmd]
    #바깥으로 이동하려하면 해당 명령 무시 
    if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
        continue 
    
    #주사위 변경 
    if cmd == 1:
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[5], dice[0], dice[4]
    elif cmd == 2:
        dice[0], dice[2], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[2]
    elif cmd == 3:
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[3], dice[5] = dice[1], dice[5], dice[0], dice[3]
        
    #이동
    x, y = nx, ny
    
    #정상적인 이동이 된다면 -> 
    #1. 지도 지도가 0 
    if mat[x][y] == 0:
        mat[x][y] = dice[5]
    #2. 지도가 0이 아닌경우
    else:
        dice[5] = mat[x][y]
        mat[x][y] = 0
        
    print(dice[0])
        
     
    
    
