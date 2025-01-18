def solution(brown, yellow):
    summ = (brown + 4)//2
    mull = yellow + brown
    
    for i in range(summ):
        if i * (summ-i) == mull:
            return [summ-i,i]

