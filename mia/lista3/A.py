q = int(input())

for _ in range(q):

  s = input().strip()
  t = input().strip()

  if t == "a":
    print(1)
  elif "a" in t:
    print(-1)
  else:
    print(2 ** len(s))
