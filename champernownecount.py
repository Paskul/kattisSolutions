# input

inputs = input().split(" ")

n = int(inputs[0])

k = int(inputs[1])

 

champernowne = 0

total = 0

 

for i in range(1, n + 1):

    # print(champernowne)

    champernowne = (champernowne * 10**(len(str(i))) + i) % k

    if champernowne == 0:

        total += 1

 

# print("\n")

print(total)
