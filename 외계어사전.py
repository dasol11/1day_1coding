def solution(spell, dic):
    for d in dic:
        if sorted(d) == sorted(spell):
            return 1
    return 2

a = solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"])
print(a)

# sorted()를 문자열에 사용하면 리스트로 반환을 한다.