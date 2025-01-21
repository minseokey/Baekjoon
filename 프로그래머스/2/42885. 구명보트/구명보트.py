def solution(people, limit):
    
    cnt = 0
    start = 0
    end = len(people) - 1
    people.sort()
    
    while end > start:
        if people[start] + people[end] <= limit:
            people[start] = -1
            people[end] = -1
            start += 1
            end -= 1
            cnt += 1
        else:
            end -= 1
    
    for i in people:
        if i != -1:
            cnt += 1
    
    return cnt
        