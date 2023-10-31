# 한번에 해결
def sol( N):
    count = 0
    
    
    for h in range(N+1):
        for m in range(60):
            for s in range(60):
                hms = str(h)+str(m)+str(s)
                if "3" in hms:
                    count +=1 
                        
        
    return count


a = sol(5)
print(a)
