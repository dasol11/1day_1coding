# 내 풀이
def solution(phone_book):
    answer = True
    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]    
                answer = False
                break
    return answer
"""
sort()를 사용하면    ["119", "97674223", "1195524421"] --> ["119", "1195524421", "97674223"]
따라서 앞뒤 데이터의 관계만 파악하면 가능함 
    
    
"""



a = solution(["119", "97674223", "1195524421"])

b = solution(["123","456","789"])

print(a)
print(b)