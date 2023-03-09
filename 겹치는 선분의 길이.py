"""
    https://school.programmers.co.kr/learn/courses/30/lessons/120876
    
    
"""




def solution(lines):
    
    sets_list = []
    
    for i in lines:
        sets = set(range(min(i),max(i)))
        sets_list.append(sets)
                   
            
    return len(sets_list[0] & sets_list[1] | sets_list[0] & sets_list[2] | sets_list[1] & sets_list[2])
    
    
a = solution([[0, 1], [2, 5], [3, 9]])
print (a)