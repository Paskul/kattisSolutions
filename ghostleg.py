n,m = [int(x) for x in input().split()]
list = range(1, n+1)

newList = []

for x in list:
    newList.append(x)
list = newList

loop = 0
while loop < m:
    a = (int(input()))
    temp = list[a]
    list[a] = list[a-1]
    list[a-1] = temp
    loop+=1

for x in list:
    print(x)
