import copy
import sys

people, party = map(int, sys.stdin.readline().split())
realpeo = set(list(map(int, sys.stdin.readline().split()))[1:])
falsepeo = set()
partylis = []

for i in range(party):
    people = list(map(int, sys.stdin.readline().split()))[1:]
    partylis.append(people)


while True:
    newreal = copy.deepcopy(realpeo)
    newfalse = copy.deepcopy(falsepeo)

    for j in partylis:
        key = True
        for k in j:
            if k in realpeo:
                realpeo = realpeo.union(set(j))
                key = False
                break
        if key:
            falsepeo = falsepeo.union(set(j))

    if newreal == realpeo and newfalse == falsepeo:
        break

ans = party
for i in partylis:
    for j in realpeo:
        if j in i:
            ans -= 1
            break

print(ans)
