a = 512
b = 191

a = 65
b = 8921

total = 0

for _ in range(40*10**6):
    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647
    if a % 2**16 == b % 2**16:
        total+=1

print(total)