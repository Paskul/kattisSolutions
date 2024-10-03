x,y,z = [int(test) for test in input().split()]

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y}

list = ['+', '-', '*', '/']
least = 100000000

first = 0
second = 0
third = 0
'''
while first < 4:
    #if ((list[first] == list[3]) & op[list[first]](x,y)%0):
    if ((list[first] == list[3]) & x%y==0):
        trying = int(op[list[first]](x,y))
    second = 0
    while second < 4:
        #if (list[second] == list[3] & trying!=0) & (op[list[second]](x,y)%0 == 0):
        if (list[second] == list[3] and (trying!=0 and (trying%z == 0))):
            if op[list[second]](trying,z) < least:
                least = int(op[list[second]](trying,z) < least)
        second+=1
    first +=1

'''
for a in list:
    if (a != list[3]) or (a == list[3] and x%y == 0):
        trying = op[a](x,y)
    else:
        pass
    for b in list:
        if b != list[3] or (b == list[3] and trying%z == 0):
            if (int(op[b](trying,z)) < least) and (int(op[b](trying,z)) >= 0):
                #print(a, b, trying, z)
                #print('found least!')
                least = op[b](trying,z)
                #print(least)

        #if (int(op[b](trying,z)) < least) and (int(op[b](trying,z)) >= 0):

print(int(least))
