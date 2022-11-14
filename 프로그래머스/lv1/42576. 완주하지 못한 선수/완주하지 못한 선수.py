def solution(participant, completion):
    participant.sort()
    completion.sort()
    i = 0
    while True:
        try:
            if participant[i] != completion[i]:
                return participant[i]
            i+=1
        except:
            return participant[-1]