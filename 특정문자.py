def solution(myString, pat):
    li = []
    m =len(myString)
    n = len(pat)
    for i in range(0,(m-n+1)):
        if myString[i:(i+n)] == pat:
            li.append(i+n)  
    return myString[:max(li)]


def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

pat = "dE"
print(pat[::-1])
myString = "AbCdEFG" 
print(myString[::-1])