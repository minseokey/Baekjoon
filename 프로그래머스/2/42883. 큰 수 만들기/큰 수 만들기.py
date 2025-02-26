from collections import deque


def solution(number, k):
    numbers = [i for i in number]
    a = deque()
    count = 0
    index = 1
    a.append(numbers[0])
    while count < k and index < len(numbers):
        temp = numbers[index]
        while count < k:
            if len(a) > 0 and a[len(a)-1] < temp:
                a.pop()
                count += 1
            else:
                a.append(temp)
                break
        index += 1
    return "".join((list(a) + numbers[index-1:])[:len(numbers)-1])











