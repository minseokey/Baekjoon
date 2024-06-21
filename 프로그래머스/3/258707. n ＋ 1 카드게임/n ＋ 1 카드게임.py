def thereSuc(coin):
    # 우선순위?
    # 1. 처음에 든거 두개
    breakey = False
    if not breakey and have:
        for i in range(len(have)):
            for j in range(i, len(have)):
                if have[i] + have[j] == target:
                    have.pop(i)
                    have.pop(j-1)
                    breakey = True
                    break
            if breakey:
                break
    # 2. 처음에든거 하나, 손에 든거 하나 (coin -= 1)
    if not breakey and coin >= 1 and have:
        for i in range(len(have)):
            for j in range(len(hand)):
                if have[i] + hand[j] == target:
                    have.pop(i)
                    hand.pop(j)
                    coin -= 1
                    breakey = True
                    break
            if breakey:
                break

    # 3. 손에 든거 두개 (coin -= 2)
    if not breakey and coin >= 2:
        for i in range(len(hand)):
            for j in range(i, len(hand)):
                if hand[i] + hand[j] == target:
                    hand.pop(i)
                    hand.pop(j-1)
                    coin -= 2
                    breakey = True
                    break
            if breakey:
                break

    # breakey = False -> 못뺐다. 종료
    if not breakey:
        coin = -1
    
    return coin

def solution(coin, cards):
    global have,hand,target
    target = len(cards) + 1
    have = cards[:target // 3]
    left = cards[target // 3:]
    hand = []
    game_round = 1
    leftcoin = coin
    for i in range(0, len(left), 2):
        hand.append(left[i])
        hand.append(left[i + 1])
        # 여기서 have+hand 가 target이 되는것을 뺀다 -> 여기서부터 백트래킹? 아니지
        # 여기서 빼는것이 어차피 더해지는것이기때문에 다른경우가 없다 -> 그리디.
        leftcoin = thereSuc(leftcoin)
        if leftcoin < 0 :
            break
        else:
            game_round += 1
    return game_round

