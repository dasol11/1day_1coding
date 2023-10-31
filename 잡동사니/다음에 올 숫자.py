def solution(common):
    One , Two , Three = common[:3]
    if Two - One == Three - Two:
        answer = common[-1] + (Three - Two)
    elif Two // One == Three// Two: # elif를 if로 해서 못했엇음 
        answer = common[-1] * (Three // Two)
    
    return answer