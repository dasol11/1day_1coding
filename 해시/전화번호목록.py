def solution(phone_book):
    phone_book.sort()
    
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    
    return True
"""
sort()를 사용하면    ["119", "97674223", "1195524421"] --> ["119", "1195524421", "97674223"]
따라서 앞뒤 데이터의 관계만 파악하면 가능함 
    
    
"""



a = solution(["119", "97674223", "1195524421"])

b = solution(["123","456","789"])

print(a)
print(b)