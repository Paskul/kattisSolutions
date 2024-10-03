r, c = [int(x) for x in input().split()]

total = r
for col in range(c-1):
    total *= (r-1)
    total= (total%998244353)

print(total)
