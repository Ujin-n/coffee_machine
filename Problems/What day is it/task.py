offset = int(input())

hours = 10
diff = hours + offset

if diff > 23:
    print("Wednesday")
elif diff < 0:
    print("Monday")
else:
    print("Tuesday")
