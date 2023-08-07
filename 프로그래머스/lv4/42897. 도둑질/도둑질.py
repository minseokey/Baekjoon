def solution(money):
    # 두가지 경우의 수를 만들자. -> 시작을 체크하고 가던지, 아니던지.
    dpTrue = [[0,0] for _ in range(len(money))]
    dpFalse = [[0,0] for _ in range(len(money))]
    
    dpTrue[0] = [money[0],0]
    dpFalse[0] = [0,0]
    
    for i in range(1, len(money)):
        doT = dpTrue[i-1][0]
        noT = dpTrue[i-1][1]
        
        doF = dpFalse[i-1][0]
        noF = dpFalse[i-1][1]
        
        
        dpTrue[i][1] = max(doT, noT)
        dpTrue[i][0] = noT + money[i]
        
        dpFalse[i][1] = max(doF, noF)
        dpFalse[i][0] = noF + money[i]
        
    tempans1 = dpTrue[-1][1]
    tempans2 = dpFalse[-1][0]
    tempans3 = dpFalse[-1][1]
    
    return (max(tempans1,tempans2,tempans3))
    