def solution(sizes):
    max_ans = 0
    min_ans = 0
    
    for a,b in sizes:
        max_a = max(a,b)
        min_b = min(a,b)
        max_ans = max(max_ans, max_a)
        min_ans = max(min_ans, min_b)
    
    return max_ans * min_ans
        