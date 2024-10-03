n = input()

valid = True
for i in range(0, len(n)):
    if int(n[i]) != i+1:
        valid = False
        break

if valid: print(len(n))
else: print(-1)
