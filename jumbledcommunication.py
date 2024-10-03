n = int(input())
bytes = input().split()
bytes = [int(i) for i in bytes]
values = []
for byte in bytes:
    for num in range(256):
        if (num^(num<<1)) & 0xFF == byte:
            values.append(num)
            break

for i in values:
    print(i)
