import itertools


def solution(users, emoticons):
    EMOLIS = [10,20,30,40]
    a = list(itertools.product([0,1,2,3], repeat=len(emoticons)))

    emoji_discount = []
    for emoticon in emoticons:
        temp = []
        for j in EMOLIS:
            temp.append(emoticon//100 * (100-j))
        emoji_discount.append(temp)

    maxx = [0,0]

    # 일단 할인정책
    for policy in a:
        userlis = [[0,False] for _ in range(len(users))]
        # 각 이모티콘별로
        for emo_ind, emo_rate in enumerate(policy):
            # 각 사람들이 이 이모티콘에 해당하는지, 또 사는지 안사는지
                for i in range(len(users)):
                    if users[i][0] <= (emo_rate+1) * 10 and not userlis[i][1]:
                        # 이러면 산다.
                        userlis[i][0] += emoji_discount[emo_ind][emo_rate]
                        if userlis[i][0] >= users[i][1]:
                            userlis[i][0] = 0
                            userlis[i][1] = True
        temp = [0,0]
        for i in userlis:
            if i[1]:
                temp[0] += 1
            else:
                temp[1] += i[0]
        maxx = max(temp,maxx)

    return maxx