from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    cnt = 0
    bridge = deque()
    truck_weights = deque(truck_weights)
    
    while truck_weights or bridge:
        
        # bridge 카운트 증가
        ind = 0
        for i in bridge:
            i[0] += 1
                
        while bridge:
            if bridge[0][0] == bridge_length:
                weight += bridge[0][1]
                bridge.popleft()
            else:
                break
        
        # bridge 에 올리기
        if len(bridge) < bridge_length and truck_weights:
            if weight >= truck_weights[0]:
                weight -= truck_weights[0]
                bridge.append([0,truck_weights.popleft()])
        
        cnt += 1
    
    return cnt
        