"""
https://school.programmers.co.kr/learn/courses/30/lessons/120812
"""




def solution(array):
    dict = {}
    for i in array:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
            
            
    result = sorted(dict.items(), key=lambda x: x[1], reverse=True)        
    if len(result)<= 1:
        return result[0][0]   
    
    if result[0][1] != result[1][1]:
        return result[0][0] 
    else:
        return -1
    



"""
Reference
https://blockdmask.tistory.com/466



sorted  :  정렬된 새로운 리스트를 반환

sort   : 기존의 리스트를 변경


some_list = [5, 7, 2, 3, 1]

print(sorted(some_list))
print(some_list.sort())
----------------
[1, 2, 3, 5, 7]
None    
-----------------
sorted(some_list)
print(some_list)
-------------------
[1, 2, 3, 5, 7]
sorted(정렬할 데이터, key 파라미터, reverse 파라미터)
--> 기본적을 오름차순(작은수부터 큰수로)

some_list = [5, 7, 2, 3, 1]


    
"""