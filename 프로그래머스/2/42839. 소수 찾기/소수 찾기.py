import itertools


def solution(numbers):
    all_length = [i for i in range(10 ** len(numbers) + 1)]
    ans = 0
    all_length[1] = 0
    for i in range(2, len(all_length)):
        if all_length[i] != 0:
            for j in range(i + i,len(all_length), i):
                all_length[j] = 0
                    
    tmp = []
    for i in range(1, len(numbers) + 1):
        for i in list(itertools.permutations(numbers,i)):
            if all_length[(int("".join(i)))] != 0:
                all_length[(int("".join(i)))] = 0
                ans += 1
    
    
    return ans
            
    
    
            