chick_price = 23
goat_price = 678
pig_price = 1296
cow_price = 3848
sheep_price = 6769

money = int(input())

if money >= sheep_price:
    quantity = money // sheep_price
    print(quantity, end='')
    print(" sheep")
elif money >= cow_price:
    quantity = money // cow_price
    print(quantity, end='')
    print(" cows" if quantity > 1 else " cow")
elif money >= pig_price:
    quantity = money // pig_price
    print(quantity, end='')
    print(" pigs" if quantity > 1 else " pig")
elif money >= goat_price:
    quantity = money // goat_price
    print(quantity, end='')
    print(" goats" if quantity > 1 else " goat")
elif money >= chick_price:
    quantity = money // chick_price
    print(quantity, end='')
    print(" chickens" if quantity > 1 else " chicken")
else:
    print("None")
