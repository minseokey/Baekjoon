def solution(arr):
    answer = []
    for i in arr:
        if len(answer) == 0 or (len(answer) > 0 and answer[-1] != i):
            answer.append(i)
    return answer