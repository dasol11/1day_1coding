

#[1, 1, 1, 1, 1]
#target	return
#	3	5

def DFS (numbers , target , depth):
    
    answer = 0
    if len(numbers) == depth:
        if sum(numbers) == target:
            return 1
        else:
            return 0

    
    else:
        answer += DFS (numbers , target , depth+1)
        numbers[depth] *= -1
        answer += DFS (numbers , target , depth+1)
        return answer
        
print(DFS([1, 1, 1, 1, 1], 3, 0))
    