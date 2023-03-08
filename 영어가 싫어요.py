"""
    
    
    
    영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, 
    numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
    
    
    numbers는 소문자로만 구성되어 있습니다.
    numbers는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.
    1 ≤ numbers의 길이 ≤ 50
    "zero"는 numbers의 맨 앞에 올 수 없습니다.
    
"""
    
    
    
def solution(numbers):
    str_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
    int_list = ["0","1","2","3","4","5","6","7","8","9"]

    for i in range(10):
        numbers = numbers.replace(str_list[i],int_list[i] )
    result= int(numbers)    
    return result

/
"""
    replace() 는 문자열을 반환해주기 때문에 
    numbers = numbers.replace(str_list[i],int_list[i] )
    위 와 같이 작성해야함 
    
    
"""