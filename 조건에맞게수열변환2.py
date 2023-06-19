def solution(arr):
    answer = 0
    la_arr = arr
    
    while True:
        no_arr = []
        for i in la_arr:
            if i % 2 == 0 and i >= 50 :
                no_arr.append(i/2)
            elif i % 2 !=0 and i < 50:
                no_arr.append(2*i+1)
            else:
                no_arr.append(i)
        if la_arr  == no_arr:
            break
        else:
            answer += 1
            la_arr = no_arr
    return answer
            
            
a = solution([1, 2, 3, 100, 99, 98])
print(a)