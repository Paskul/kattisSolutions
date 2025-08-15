runs = int(input())
found = 0
for number in input().split():
    if int(number) < 0:
        found+=1
print(found)
