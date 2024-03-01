def solution(enroll, referral, seller, amount):
    headlist = dict()
    money = dict()
    for i in range(len(enroll)):
        money[enroll[i]] = 0
        headlist[enroll[i]] = referral[i]
        
        
    def distri(who,how):
        if who == "-":
            return
        else:
            give = how//10
            mine = how - give
            money[who] += mine
            if give:
                distri(headlist[who], give)
                
    for i in range(len(seller)):
        who = seller[i]
        how = amount[i] * 100
        distri(who,how)
        
    result = []
    for i in enroll:
        result.append(money[i])
    return result