for n in range(1, 101):
    print("FizzBuzz" if n % 3 == 0 and n % 5 == 0 else "Fizz" if n % 3 == 0 else "Buzz" if n % 5 == 0 else n)
