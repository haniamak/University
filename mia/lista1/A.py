n = int(input())
count = 0
denominations  = [100, 20, 10, 5, 1]

for d in denominations:
  count += n // d
  n = n % d

print(count)
  