def solution(brown, yellow):
    # x 가로, y 세로
    for i in range(1,brown//2):
        for j in range(i,brown//2):
            if (i-2)*(j-2) == yellow and 2*(i+j-2) == brown:
                return [j,i]