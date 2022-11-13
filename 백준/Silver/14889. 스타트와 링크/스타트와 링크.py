# 일단 두팀으로 나누는게 먼저...
# 경우의수가 끝도 없을거 같은뎅..
# math.median 써야겠다 중앙값..
import sys, math, itertools
n = int(sys.stdin.readline())
table = []


def teamscore(lis):
    ans = 0
    allcase = list(itertools.combinations(lis, 2))
    for i in allcase:
        ans = ans + table[i[0]][i[1]] + table[i[1]][i[0]]
    return ans


for i in range(n):
    table.append(list(map(int, sys.stdin.readline().strip().split())))
player = [i for i in range(n)]
playerlis = itertools.combinations(player, int(n/2))

scorelis = []
for team1 in playerlis:
    teamins = set(player) - set(team1)
    team2 = list(teamins)
    scorelis.append(abs(teamscore(team1) - teamscore(team2)))

print(min(scorelis))
