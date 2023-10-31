


# numbers , target 

def DFS(numbers , target ):
    answer = 0
    leaves= [0]
    for num in numbers:
        stk = []
        for pa in leaves:
            stk.append(pa+num)
            stk.append(pa-num) 
        leaves = stk
        
        
    for leave in leaves:
        if leave == target:
            answer += 1
    return( answer )

print(DFS([1, 1, 1, 1, 1], 3))