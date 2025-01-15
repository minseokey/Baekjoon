def solution(numbers):
    n_nums = []
    for i in numbers:
        tmp = str(i)
        n_nums.append((tmp, (tmp*4)[:4]))
    
    n_nums.sort(key = lambda x:x[1], reverse = True)
    ans = ""
    for i in n_nums:
        ans += i[0]
    
    return str(int(ans))
    
    

    
