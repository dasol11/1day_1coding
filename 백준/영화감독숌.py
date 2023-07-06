n = int(input())

num = 0
for i in range(666, 666**10):
    for j in range(len(str(i))-2):
        if str(i)[j:j+3] == "666":
            num +=1
            break
    if num == n:
        print(i)
        break 