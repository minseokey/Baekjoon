def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        temp = sorted(array[commands[i][0] - 1:commands[i][1]])[commands[i][2] - 1]
        print(temp)
        answer.append(temp)
    
    return answer