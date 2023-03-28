actorList = {}
for _ in range(int(input())):
    b = input()
    actorList[b] = actorList.get(b, 0) + 1

maxStat = sorted(actorList.items(), key=lambda x: x[1], reverse=True)[0]
minStat = sorted(actorList.items(), key=lambda x: x[1])[0]
print(*maxStat, sep=', ')
print(*minStat, sep=', ')
