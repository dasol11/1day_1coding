
# 내 답안
def solution(arr):
    r = True
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                r = False
            
        
        
    return int(r)


# all을 사용한 타인 답안
def solution(arr):
    return int(all(arr[i][j] == arr[j][i] for i in range(len(arr)) for j in range(len(arr))))