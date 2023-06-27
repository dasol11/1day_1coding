def solution(bridge_length, weight, truck_weights):
    t = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        t += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight :
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return t


def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) # 트럭 무게
    x = [0] * bridge_length # 다리
    s=0
    while (x):
        time += 1
        s-=x.pop(0) # s: 다리 위의 총 트럭 무게
        if p:
            if ( s + p[0] ) <= weight:
                s+=p[0] # 여유되면 트럭 추가
                x.append(p.pop(0)) # 다리에 트럭 추가  
            else:
                x.append(0) # 여유 없으면 무게 0 추가

    return time

a = solution(2,10,[7,4,5,6])
print(a)


