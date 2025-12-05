t = int(input())

for _ in range(t):
  n = int(input())

  if n % 2 == 1:
    print(0)
    continue
  else:
    cows = n // 4
    print(cows + 1)
