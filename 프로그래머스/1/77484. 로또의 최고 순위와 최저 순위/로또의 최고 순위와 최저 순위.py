def solution(lottos, win_nums):
    c_zero = 0
    c_correct = 0
    
    for i in lottos:
        if i == 0:
            c_zero += 1
        elif i in win_nums:
            c_correct += 1
    
    b,l = 0,0
    if c_correct == 0:
        l = 6
    else:
        l = 7-c_correct
    if c_correct + c_zero == 0:
        b = 6
    else:
        b = 7 - (c_correct + c_zero)
    return [b,l]