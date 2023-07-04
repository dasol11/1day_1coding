n = 1
while n :
    n, m = map(int,input().split())
    if n == 0 or m==0:
        break
    elif n % m ==0 :
        print("multiple")
    elif m % n == 0:
        print("factor")
    else:
        print("neither")
    
    