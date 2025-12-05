n = int(input())
a, b = map(int, input().split())

def get_divisors(x):
  divs = set()
  d = 2
  while d * d <= x:
    if x % d == 0:
      divs.add(d)
      while x % d == 0:
        x //= d
    d += 1
  if x > 1:
    divs.add(x)
  return divs

pairdivs = list(get_divisors(a)) + list(get_divisors(b))
validdivs = set(pairdivs)

for _ in range(n - 1):
  x, y = map(int, input().split())
  remove = []
  for d in validdivs:
    if x % d != 0 and y % d != 0:
      remove.append(d)
  for d in remove:
    validdivs.remove(d)

if len(validdivs) > 0:
  print(next(iter(validdivs)))
else:
  print(-1)