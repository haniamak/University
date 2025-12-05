t = int(input())

for _ in range(t):
  n = int(input())
  seen = set()
  moves = 0
  a = list(map(int, input().split()))
  for i in range(len(a)):
    while a[i] % 2 == 0:
      if a[i] not in seen:
        seen.add(a[i])
        a[i] //= 2
        moves += 1
      else:
        break
  print(moves)
