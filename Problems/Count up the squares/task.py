num_list = []
num_sq_list = []
while True:
    number = int(input())
    num_list.append(number)
    num_sq_list.append(number ** 2)
    if sum(num_list) == 0:
        break

print(sum(num_sq_list))
