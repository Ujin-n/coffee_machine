def is_prime(n):
    if n == 1:
        return False

    d = 2
    while n % d != 0:
        d += 1
    return d == n


if is_prime(int(input())):
    print("This number is prime")
else:
    print("This number is not prime")
