n = int(input())
valid = True
for i in range(3):
    testing = [int(x) for x in input().split()]
    if 7 not in testing:
        valid = False
    
if valid: print(777) 
else: print(0)
