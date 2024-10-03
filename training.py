n, s = [int(x) for x in input().split()]
curSkill = s
for i in range(n):
    low, high = [int(x) for x in input().split()]
    if (low <= curSkill) and (curSkill <= high):
        curSkill+=1

print(curSkill)
