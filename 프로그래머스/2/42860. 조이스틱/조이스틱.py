def solution(name):
    change_cost = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)
    
    leng = len(name)
    min_move = leng - 1  # 최악의 경우: 오른쪽으로만 쭉 이동

    for i in range(leng):
        # 현재 위치에서 오른쪽으로 i칸 이동 후, 남은 문자열에서 A를 제외한 끝에서 돌아오는 경우
        next_i = i + 1
        while next_i < leng and name[next_i] == 'A':
            next_i += 1
        distance = i + leng - next_i + min(i, leng - next_i)
        min_move = min(min_move, distance)

    return change_cost + min_move
