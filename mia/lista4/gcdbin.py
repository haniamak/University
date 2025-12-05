def gcdbin(a, b):
  if a == 0 and b == 0:
    return KeyError("GCD is not defined for both numbers being zero.")
  # if a == 0 or b == 0:
  #   return max(a, b)
  if a == b:
    return a
  if a % 2 == 0 and b % 2 == 0:
    return 2 * gcdbin(a // 2, b // 2)
  if a % 2 == 0 and b % 2 == 1:
    return gcdbin(a // 2, b)
  if a % 2 == 1 and b % 2 == 0:
    return gcdbin(a, b // 2)
  if a % 2 == 1 and b % 2 == 1 and a > b:
    return gcdbin(a - b, b)
  if a % 2 == 1 and b % 2 == 1 and a < b:
    return gcdbin(a, b - a)

print(gcdbin(45, 15))
