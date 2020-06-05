x = float(input())
y = float(input())

if y > 0:
    if x < 0:
        print("II")
    elif x > 0:
        print("I")
elif y < 0:
    if x < 0:
        print("III")
    elif x > 0:
        print("IV")
