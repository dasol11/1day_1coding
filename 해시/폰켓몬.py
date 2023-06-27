def solution(nums):
    unique_types = len(set(nums))

    if len(nums) / 2 > unique_types:
        return unique_types
    else:
        return len(nums) / 2

a =solution([3,1,2,3])
b = solution([3,3,3,2,2,4])