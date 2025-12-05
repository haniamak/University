t = int(input())
import math

for _ in range(t):
  total = 0
  n, h = map(int, input().split())
  a = list(map(int, input().split()))

  kmin = math.ceil(h / n)
  
  l, r = kmin, h
  while l < r:
    mid = (l + r) // 2
    total = mid
    for i in range(len(a) - 1):
      total += min(mid, a[i+1] - a[i])
      if total >= h:
        break
    if total >= h:
      r = mid
    else:
      l = mid + 1
  
  print(l)