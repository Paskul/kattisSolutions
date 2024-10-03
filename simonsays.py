runs = int(input())
for i in range(runs):
    line = input()
    if line.startswith('simon says'):
        print(line[11:])
