t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  if a[-1] == a[0] == -1:
    suma = 0
    a[0] = 0
    a[-1] = 0
    
  elif a[-1] == -1:
    a[-1] = a[0]
    suma = 0
  elif a[0] == -1:
    a[0] = a[-1]
    suma = 0
  else:
    suma = abs(a[-1] - a[0])
  print(suma)
  for i in range(len(a)):
      if a[i] == -1:
        a[i] = 0
  print(" ".join(str(x) for x in a))