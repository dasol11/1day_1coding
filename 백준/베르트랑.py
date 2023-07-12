# import sys

# input = sys.stdin.readline
# def prime_list(n):
#     # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
#     sieve = [True] * n

#     # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
#     m = int(n ** 0.5)
#     for i in range(2, m + 1):
#         if sieve[i] == True:           # i가 소수인 경우
#             for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
#                 sieve[j] = False

#     # 소수 목록 산출
#     return [i for i in range(2, n) if sieve[i] == True]
# stk = prime_list(123456*2)

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     answer = 0
#     for i in range(n+1, 2*n+1):
#         if i in stk:
#             answer += 1
#     print(answer)
        
        
import sys

input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i ==0:
            return False
    return True
prime_list = [i for i in range(2, 2*123456 + 1) if is_prime(i)]

while True:
    n = int(input())
    if n == 0:
        break
    
    answer = 0
    for i in prime_list:
        if n < i <= 2*n:
            answer += 1
    print(answer)       
    