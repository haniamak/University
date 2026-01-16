t = int(input())


def sum_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


for _ in range(t):
    n = int(input())
    sumn = sum_digits(n)
    while gcd(n, sumn) == 1:
        n += 1
        sumn = sum_digits(n)
    print(n)
