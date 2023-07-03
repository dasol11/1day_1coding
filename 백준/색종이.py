arr = [[0 for _ in range(100)]for _ in range(100)]


for _ in range(int(input())):
    n,m = input().split()
    for i in range(int(n),int(n)+10):
        for j in range(int(m),int(m)+10):
            arr[i][j] = 1

print(sum([sum(i)for i in arr]))
