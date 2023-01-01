def solution(people, limit):
    people.sort(reverse = True)
    count = 0
    i = 0 # 앞에서부터 추적
    j = len(people) - 1 # 뒤에서 추적
    while True:
        if i > j:
            break
        count += 1
        if people[i] + people[j] <= limit:
            j -= 1
        i += 1

    return count
