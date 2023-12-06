def solution(cap, n, deliveries, pickups):
    gkey, tkey = True, True
    give_point, take_point = 0,0
    for i in range(n - 1, -1, -1):
        if gkey and deliveries[i] != 0:
            give_point = i
            gkey = False
        if tkey and pickups[i] != 0:
            take_point = i
            tkey = False
        if not gkey and not tkey:
            break
    path = 0
    if not give_point and not take_point:
        return 0
    while give_point >= 0 or take_point >= 0:
        # 가장 먼것부터 주자.
        path += 2 * (max(give_point, take_point) + 1)
        temp_give_counter = cap
        while temp_give_counter >= 0 and give_point >= 0:
            if deliveries[give_point] <= temp_give_counter:
                temp_give_counter -= deliveries[give_point]
                give_point -= 1
            else:
                deliveries[give_point] -= temp_give_counter
                break

        # 가장 먼것부터 가져오자.
        temp_take_counter = cap
        while temp_take_counter >= 0 and take_point >= 0:
            if pickups[take_point] <= temp_take_counter:
                temp_take_counter -= pickups[take_point]
                take_point -= 1
            else:
                pickups[take_point] -= temp_take_counter
                break
    return path