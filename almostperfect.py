from math import sqrt
import sys

def findDivisors(val):
    count = 1
    for i in range(2, int(sqrt(val)+1)):
        if val%i == 0:
            count+=i
            if(i*i != val):
                count += val // i
    return count

def printing(i):
    use = findDivisors(i)
    if use == i:
        print(i, 'perfect')
    elif abs(i-use)<=2:
        print(i, 'almost perfect')
    else:
        print(i, 'not perfect')

for line in sys.stdin.readlines():
    line = int(line)
    printing(line)
