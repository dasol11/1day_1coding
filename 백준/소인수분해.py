n = int(input())

while n != 1:
    for i in range(2,n+1):
        if n % i == 0:            
            n = int(n / i)
            print(i, n)
            break