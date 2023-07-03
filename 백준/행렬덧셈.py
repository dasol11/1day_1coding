

n,m = map(int,input().split())
a = []
b = []
for _ in range(n):
    li = list(map(int,input().split()))
    a.append(li)
    
for _ in range(n):
    li = list(map(int,input().split()))
    b.append(li)

for i, j in zip(a,b):
    st = ""
    for k, l in zip(i,j):
        st += str(str(k+l) + " ")
    print(st)