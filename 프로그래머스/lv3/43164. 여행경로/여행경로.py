import copy


def solution(tickets):
    ticketdic = {}
    for i in tickets:
        if i[0] in ticketdic.keys():
            ticketdic[i[0]].append(i[1])
        else:
            ticketdic[i[0]] = [i[1]]

    anss = []

    def dfs(ticket, answer, now):
        if len(answer) == len(tickets) + 1:
            anss.append(answer)
            return
        
        if not now in ticket.keys():
            return 
        
        for i in ticket[now]:
            newtic = copy.deepcopy(ticket)
            newans = copy.deepcopy(answer)
            newtic[now].remove(i)
            newans.append(i)
            dfs(newtic, newans, i)

    for i in ticketdic["ICN"]:
        ntic = copy.deepcopy(ticketdic)
        ntic["ICN"].remove(i)
        dfs(ntic, ["ICN", i], i)

    return min(anss)