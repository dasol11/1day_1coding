while True:
    li =list(map(int,input().split()))
    li.sort()
    if li[0]==0:
        break
    else:
        if li[2] >= (li[1]+li[0]):
                print("Invalid")   
        else:
            if li[0]==li[1]==li[2]:
                print("Equilateral")
            elif li[0] == li[1] or li[2] ==li[1] or li[0]==li[2]:
                print("Isosceles")
            else:    
                print("Scalene")
     