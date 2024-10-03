import math

line = input()
line = line.split()
line = list(map(int,line))

rads = line[1] * (math.pi/180)

output = line[0]/(math.sin(rads))
output = math.ceil(output)
print(output)
