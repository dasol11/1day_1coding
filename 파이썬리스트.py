"""
    파이썬 리스트 슬라이싱
* [:] 처음부터 끝까지
* [start:] start오프셋(인덱스)부터 끝까지
* [:end] 처음부터 end-1 오프셋(인덱스)까지 
* [start : end] start오프셋부터 end-1 오프셋(인덱스)까지
* [start : end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출

    
    join에 조건문을 활용하여서 사용가능
    
    [i for ~~ 조건문 ~~ if 문]
"""


def solution(str_list, ex):
    return  "".join(i for i in str_list if ex not in i)



def solution1(arr):
    return [i for i in arr for _ in range(i)]
# arr 안에 원소를 꺼내서 원소만큼 반복하면서 j 포문이 돌때마다 원소를 추가함 

b = solution1([5, 1, 4])
print(b)
#[5, 5, 5, 5, 5, 1, 4, 4, 4, 4]


