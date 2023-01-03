def solution(numbers):
    for i,n in enumerate(numbers):
        numbers[i] = {"".join([str(n) for x in range(4)])[:4]:str(n)}

    answer = ""
    numbers.sort(key = lambda x : list(x.keys()),reverse=True)
    for i in numbers:
        answer += list(i.values())[0]

    i = 0
    while i < len(answer) and answer[i] == '0':
        i += 1

    answer = answer[i:]
    if answer == "":
        return "0"

    return answer