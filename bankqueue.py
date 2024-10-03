n, t = [int(x) for x in input().split()]

peopleDict = {}

for i in range(n):
    ci, ti = [int(x) for x in input().split()]
    if ti in peopleDict.keys():
        test = peopleDict[ti]
        test.append(ci)
        peopleDict[ti] = test
    else:
        peopleDict[ti] = [ci]

possibleOptions = []
total = 0
for i in range(t, -1, -1):
    if i in peopleDict.keys():
        for j in peopleDict[i]:
            possibleOptions.append(j)
    if possibleOptions:
        total += max(possibleOptions)
        possibleOptions.remove(max(possibleOptions))

print(total)
