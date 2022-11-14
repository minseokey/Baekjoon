def solution(clothes):
    a = dict()
    for i in clothes:
        if i[1] not in a:
            a.update({i[1]:1})
        else:
            a[i[1]] += 1
    
    answer = 1
    
    for i in a.values():
        answer *= i+1
    
    return answer - 1