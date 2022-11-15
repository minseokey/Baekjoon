def solution(s):
    answer = True
    a = []
    for i in s:
        if i == "(":
            a.append("(")
        else:
            try:
                a.pop(-1)
            except:
                answer = False
    if a:
        answer = False
    print('Hello Python')

    return answer