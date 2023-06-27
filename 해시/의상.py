# 내 코드
def solution(clothes):
    dic = {}
    d = 1
    for name, type in clothes:
        if type  not in dic:
            dic[type] = [name]
        else:
            dic[type].append(name)
            
    for key in dic.values():
        d *= (len(key) +1)

    return d -1
"""
   [바지, 청바지, 반바지] [흰티, 검은티, 회색티]  
    각 바지와 티를 조합한 결과 3 * 3 = 9 
   각 하나씩 입었을대 6  총 15
   
   [바지, 청바지,반바지] [흰티, 검은티,]
    6 + 5 = 11
   
    즉, (n +1) * (m+1) -1 --> d *= (len(key) +1)
    
"""





a = solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
print(a)
b = solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])
print(b)

c = solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"],
              ["green_turban", "headgear"], ["yellow_hat", "headgear"],["red_hat", "headgear"]])
print(c)