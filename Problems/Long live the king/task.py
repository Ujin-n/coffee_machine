y = int(input())
x = int(input())

if x in (1, 8) and y in (1, 8):
    print(3)
elif (1 < x < 8) and (1 < y < 8):
    print(8)
else:
    print(5)
