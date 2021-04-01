# https://www.acmicpc.net/problem/6603
# boj 1248 S2 6603
# <메모리 : 123156, 시간 136>

import sys
from itertools import combinations
input = sys.stdin.readline
'''
- lst가 없을떄가 존재하는 모양이다 
- 만약 lst가 있는 경우만 출력을해주고, 없는 경우에는 break 시켜줘야 통과가 되는데 이유를 절대 모르겠다
- 맨붕...
'''

while True:
    a = input()
    if a == '0':
        break 
    
    lst = list(map(int, a.split()))
    
    if lst:
        k = lst[0]
        s = lst[1:]

        for item in list(combinations(s, 6)):
            print(str(item).replace(',','').replace('(','').replace(')',''))
        print()
    else:
        break 
    
    
    
    
        