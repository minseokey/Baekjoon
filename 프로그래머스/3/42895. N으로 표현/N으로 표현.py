from collections import defaultdict

def solution(N, number):
    
    dic = defaultdict(set)
    dic[1].add(N)
    
    if N == number:
        return 1

    for i in range(2,9):
        # i 기준 낮은 수 두개끼리 사칙연산 수행.
        dic[i].add(int(str(N) * i))
        for j in range(1, i):
            for fir in dic[i-j]:
                for sec in dic[j]:
                    dic[i].add(fir + sec)
                    dic[i].add(fir - sec)
                    dic[i].add(fir * sec)
                    if sec != 0:
                        dic[i].add(fir // sec)
        
        if number in dic[i]:
            return i

    return -1
    


            