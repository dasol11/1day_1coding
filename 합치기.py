n = int(input())
count = 0
while count < n:
    a, b = map(int, input().split())
    count += 1
    result = a+b
    print("Case #{}: {}".format(count,result))
