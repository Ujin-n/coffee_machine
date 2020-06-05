a = int(input())
b = int(input())

total = 0
quantity = 0
for n in range(a, b + 1):
    if n % 3 == 0:
        total += n
        quantity += 1

print(total / quantity)
