a = 0
b = 0

for _ in range(30):
    s = input().split()
    
    if s[2] != "P":
        a += float(s[1])
    if s[2] == "A+":
        c = 4.5
    elif s[2] == "A0":
        c = 4
    elif s[2] == "B+":
        c = 3.5
    elif s[2] == "B0":
        c = 3
    elif s[2] == "C+":
        c = 2.5
    elif s[2] == "C0":
        c = 2
    elif s[2] == "D+":
        c = 1.5
    elif s[2] == "D0":
        c = 1
    else:
        c = 0
    b += float(s[1]) * c
    
print (b/a)       