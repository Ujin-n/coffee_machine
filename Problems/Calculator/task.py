first_num = float(input())
second_num = float(input())
arith_operator = input()

if arith_operator == "+":
    print(first_num + second_num)
elif arith_operator == "-":
    print(first_num - second_num)
elif arith_operator == "*":
    print(first_num * second_num)
elif arith_operator == "pow":
    print(first_num ** second_num)
elif second_num == 0:
    print("Division by 0!")
elif arith_operator == "/":
    print(first_num / second_num)
elif arith_operator == "mod":
    print(first_num % second_num)
elif arith_operator == "div":
    print(first_num // second_num)
