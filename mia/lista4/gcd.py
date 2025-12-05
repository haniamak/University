def gcd(a, b):
    if a == 0 and b == 0:
        return KeyError("GCD is not defined for both numbers being zero.")
    while b:
        a, b = b, a % b
    return a

print(gcd(3, 0))  # Example usage

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b

print(lcm(3, 0))  # Example usage
print(lcm(3, 4))  # Example usage
print(lcm(2, 4))  # Example usage