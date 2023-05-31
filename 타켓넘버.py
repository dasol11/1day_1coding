def solution(numbers, target):
    answer = 0
    stack = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    
    while stack :
        num, idx = stack.pop()
        idx += 1
        if idx < n:
            stack.append([(num + numbers[idx]),idx])
            stack.append([(num - numbers[idx]),idx])
        else:
            if num == target:
                answer += 1
    return answer

