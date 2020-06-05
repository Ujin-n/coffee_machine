num_list = []
while True:
    number = int(input())
    if number > 100:
        break
    if number >= 10:
        num_list.append(number)

for n in num_list:
    print(n)
