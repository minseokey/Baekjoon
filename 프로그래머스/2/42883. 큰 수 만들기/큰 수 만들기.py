def solution(number, k):
    stack = []
    for i in number:
        while k > 0:
            if stack and stack[-1] < i:
                stack.pop()
                k -= 1
            else:
                break
        stack.append(i)
    
    return "".join(stack[:len(stack) - k])
            
