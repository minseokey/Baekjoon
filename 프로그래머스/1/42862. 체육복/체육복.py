def solution(n, lost, reserve):
    allStu = [1 for _ in range(n)]
    for i in reserve:
        allStu[i-1] += 1
    for i in lost:
        allStu[i-1] -= 1
        
    for i in range(len(allStu)):
        if allStu[i] == 2:
            # 작은쪽부터 옷을 주자.
            if i-1 >= 0 and allStu[i-1] == 0:
                allStu[i-1] = 1
                allStu[i] = 1
            elif i+1 < len(allStu) and allStu[i+1] == 0:
                allStu[i+1] = 1
                allStu[i] = 1
    
    ans = 0
    for i in allStu:
        if i != 0:
            ans += 1
    
    return ans