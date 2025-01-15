from collections import defaultdict

def solution(participant, completion):
    dic = defaultdict(int)
    for i in participant:
        dic[i] += 1
    
    for i in completion:
        dic[i] -= 1
        if dic[i] == 0:
            dic.pop(i)
    
    print(dic.keys())
    return list(dic.keys())[0]
        
    