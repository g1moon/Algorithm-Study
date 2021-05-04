'''
- 두 집합의 교집합 크기 / 두 집합의 합집합 크기 
- 공집합인 경우 -> 유사도는 1
- 
'''


str1 = 'FRANCE'	
str2 = 'french'		
str1 = 'handshake'	
str2 = 'shake hands'		
str1 = 'aa1+aa2'	
str2 = 'AAAA12'		

from string import ascii_lowercase
import copy 
alpLst = list(ascii_lowercase)

def solution(str1, str2):
    ans = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    firLst = list(str1.lower())
    secLst = list(str2.lower())
    

    tmp1, tmp2 = [], []
    
        
    for i in range(0, len(firLst)-1):
        t1 = ''
        t1 = firLst[i] + firLst[i+1]
        for i in range(2):
            if t1[i] not in alpLst:
                break  
        else:
            tmp1.append(t1)
        
    
    for i in range(0, len(secLst)-1):
        t2 = ''
        t2 = secLst[i] + secLst[i+1]
        for i in range(2):
            if t2[i] not in alpLst:
                break
        else:
            tmp2.append(t2)

    firLst = copy.deepcopy(tmp1)
    secLst = copy.deepcopy(tmp2)
    

    
    dic1, dic2 = {}, {} 
    for s in firLst:
        if s in dic1.keys():
            dic1[s] += 1 
        else:
            dic1[s] = 1 
            
    for s in secLst:
        if s in dic2.keys():
            dic2[s] += 1 
        else:
            dic2[s] = 1 

    #count 
    a, b = 0, 0 
    
    #교    
    for i in set(firLst+secLst):
        if i in dic1.keys() and i in dic2.keys():
            a += min(dic1[i], dic2[i])
            b += max(dic1[i], dic2[i])
            
        elif (i in dic1.keys()) and (i not in dic2.keys()):
            b += dic1[i]
            
        else:
            b += dic2[i]
        
    if a == 0 and b == 0:
        ans = 1 * 65536
    else:
        ans = int((a/b)*65536)
    return ans


print(solution(str1, str2))