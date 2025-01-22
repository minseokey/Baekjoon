def solution(numbers, target):
    
    queue = [(0,0)]
    ans = 0
    
    while queue:
        summ, ind = queue.pop()
        if ind == len(numbers) and summ == target:
            ans += 1
            continue
        elif ind < len(numbers):
            now = numbers[ind]
            queue.append((summ+now, ind+1))
            queue.append((summ-now, ind+1))
    
    return ans