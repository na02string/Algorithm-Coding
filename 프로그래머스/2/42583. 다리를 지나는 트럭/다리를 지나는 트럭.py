def solution(bridge_length, weight, truck_weights):
    answer = 0
    from collections import deque
    truck_weights = deque(truck_weights)
    bridge = deque(0 for i in range(bridge_length))
    bridge_weight = 0 # 다리위에 올라가 있는 차 무게
    check_finish = []
    while True:
        new = bridge.popleft()
        bridge_weight -= new
        if truck_weights:
            
            if truck_weights[0] + bridge_weight > weight :
                bridge.append(0)
                answer += 1
            else:
                new = truck_weights.popleft()
                bridge_weight += new
                bridge.append(new)
                answer  += 1
        else:   
            while bridge:
                answer += 1
                bridge.popleft()
            break
            
    return answer+1