n ,m = map(int, input().split())

bak = [str(i) for i in range(1,n +1)]

for _ in range(m):
    a ,b = map(int, input().split())
    
    bak[a-1] , bak[b-1] =     bak[b-1] , bak[a-1]
    print(bak)
print(" ".join(bak))