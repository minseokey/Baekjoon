import collections

def solution(bridge_length, weight, truck_weights):
    truck_weights = collections.deque(truck_weights)
    queue = collections.deque()
    for i in range(bridge_length):
        queue.append(0)
    time = 0
    allout = 0
    allin = sum(truck_weights)
    queuein = 0
    while True:
        time += 1
        allout += queue.popleft()
        if truck_weights:
            if queuein - allout + truck_weights[0] > weight:
                queue.append(0)
            else:
                tempa = truck_weights.popleft()
                queuein +=tempa
                queue.append(tempa)
        else:
            if allin == allout:
                break
    return time
