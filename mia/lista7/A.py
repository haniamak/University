n = int(input())

t = list(map(int, input().split()))

counter = 1
res = []

for i in range(1, n):
  if t[i] == t[i - 1]:
    counter += 1
  else:
    res.append(counter)
    counter = 1
res.append(counter)

length = 0
for i in range(len(res) - 1):
  length = max(length, 2 * min(res[i], res[i + 1]))
  
print(length)

