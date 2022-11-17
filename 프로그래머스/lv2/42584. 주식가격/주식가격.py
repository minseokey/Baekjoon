import collections
def solution(prices):
    pricesdeque = collections.deque(prices)
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)):
        temp = pricesdeque.popleft()
        for j in range(i+1,len(prices)):
            answer[i] += 1
            if prices[j] >= temp:
                pass
            else:
                break
    return(answer)