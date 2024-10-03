n = int(input())

treesString = input().split()
treeList = [int(x) for x in treesString]

treeList.sort(reverse=True)
dayMax = 1
for i in range(len(treeList)):
    curr = i + treeList[i]
    #print(curr)
    if curr > dayMax:
        dayMax = curr

print(dayMax+2)
