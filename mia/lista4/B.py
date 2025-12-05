q = int(input())

for _ in range(q):

  s = str(input())
  t = str(input())
  y = 0

  for i in range(len(s)):
    for j in range(len(s) - i):
      l = len(t) - 1 - j
      if i + j < l:
        continue
      f1p = i
      f1k = i + j
      f2p = f1k - l
      if s[f1p:f1k + 1] + s[f2p:f1k][::-1] == t:
        y = 1

  print("YES" if y else "NO")

