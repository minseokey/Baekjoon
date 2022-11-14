import  heapq


def solution(operations):
    ansQueueMax = []  # max heap
    ansQueueMin = []  # min heap
    allist = []
    for i in range(len(operations)):
        command, number = operations[i].split()
        number = int(number)

        if command == "D":
            if number == -1:
                while ansQueueMin:
                    temp = heapq.heappop(ansQueueMin)
                    if temp in allist:
                        allist.remove(temp)
                        break
            elif number == 1:
                while ansQueueMax:
                    temp = -heapq.heappop(ansQueueMax)
                    if temp in allist:
                        allist.remove(temp)
                        break
        else:
            heapq.heappush(ansQueueMax, -number)
            heapq.heappush(ansQueueMin, number)
            allist.append(number)

    if not allist:
        return [0,0]
    else:
        return [max(allist), min(allist)]