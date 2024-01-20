from collections import deque
def getMaxTrafficTime(start, end):
    
    t = 1
    que = deque()
    Max = max(end)
    que_max = 0
    result_t = 0
    while t <= Max:
        
        for s in start:
            if t == s:
                que.append(s)
                
        l = len(que)
        if l > que_max:
            result_t = t
            que_max = l       
        
        for e in end:
            if t == e:
                que.pop()
                
                
        l = len(que)
    
        if l > que_max:
            result_t = t
            que_max = l
          
         
        print(t, que)
        t += 1  
    return result_t


print(getMaxTrafficTime([2,3,7,4,7], [4,5,8,7,10]))

print(getMaxTrafficTime([1,1,1],[5,5,5]))