def solution(answers):
    p_1 = [1,2,3,4,5] * 2000
    p_2 = [2,1,2,3,2,4,2,5] * 1250
    p_3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    
    c_1 = 0
    c_2 = 0
    c_3 = 0
    
    for i in range(len(answers)):
        if p_1[i] == answers[i]:
            c_1 += 1
            
        if p_2[i] == answers[i]:
            c_2 += 1
            
        if p_3[i] == answers[i]:
            c_3 += 1
    
    maxx = max(c_1, c_2, c_3)

    ans = []
    if c_1 == maxx:
        ans.append(1)
    if c_2 == maxx:
        ans.append(2)
    if c_3 == maxx:
        ans.append(3)
    
    return sorted(ans)
    
