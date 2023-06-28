#DFS 풀이
def DFS(numbers, target, depth):
    answer = 0
    if depth != len(numbers):
        answer += DFS(numbers, target, depth+1)
        numbers[depth] *= (-1)
        answer += DFS(numbers, target, depth+1)
        return answer
    else:
        if sum(numbers) == target:
            return 1
        else:
            return 0
        
    
def solution(numbers, target):
    answer = DFS(numbers, target, 0)
    return answer


a = solution([1, 1, 1, 1, 1],3 )
print(a)