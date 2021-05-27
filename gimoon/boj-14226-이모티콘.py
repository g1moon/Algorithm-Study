import sys
from collections import deque
input = sys.stdin.readline

'''
1. 화면에 있는 이모티콘 모두 복사 -> 클립보드 저장
2. 붙여넣기 
3. 화면에 있는 이모티콘 중 하나 삭제
'''

def copyEmg(num, cb, c):
    return num, num, c+1

def pasteEmg(num, cb, c):
    return num + cb, cb, c+1

def delEmg(num, cb, c):
    if num == 0:
        return num, cb, c+1    
    else:
        return num-1, cb, c+1
    


if __name__ == "__main__":
    s = int(input())
    cnt= 0
    cur = 1
    board = 0
    q = deque()
    
    q.append(copyEmg(cur, board, cnt))
    q.append(delEmg(cur, board, cnt))
    
    ckMat = [[0]*2000 for _ in range(2000)]
    ckMat[cur][board] = 1
    ckMat[cur-1][board] = 1
    
    funcLst = [copyEmg, delEmg, pasteEmg]
    

    while q: 
        cur, board, cnt = q.popleft()
        
        if cur == s:
            print(cnt)
            break 
        
        for func in funcLst:
            tcur, tboard, tcnt = func(cur, board, cnt)
            try:
                if ckMat[tcur][tboard] == 0:
                    ckMat[tcur][tboard] = 1
                    q.append((tcur, tboard, tcnt))
            except:
                pass
        
        
        # tcur, tboard, tcnt = copyEmg(cur, board, cnt)
        # try:
        #     if ckMat[tcur][tboard] == 0:
        #         ckMat[tcur][tboard] = 1
        #         q.append((tcur, tboard, tcnt))
        # except:
        #     pass
        

        # tcur, tboard, tcnt = delEmg(cur, board, cnt)
        # try:
        #     if ckMat[tcur][tboard] == 0:
        #         ckMat[tcur][tboard] = 1
        #         q.append((tcur, tboard, tcnt))
        # except:
        #     pass
            
            
        # tcur, tboard, tcnt = pasteEmg(cur, board, cnt)
        # try:
        #     if ckMat[tcur][tboard] == 0:
        #         ckMat[tcur][tboard] = 1
        #         q.append((tcur, tboard, tcnt))
        # except:
        #     pass
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    


    
    
    