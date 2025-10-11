tests = int(input())

for _ in range(tests):
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))
  
  allbanknotes = k + 1
  res = 0
  
  
  for i in range(n):
    baknotestouse = allbanknotes
    if i + 1 < n:
      baknotestouse = min(baknotestouse, 10 ** arr[i + 1] // 10 ** arr[i] - 1)
      #print(baknotestouse)
    res += (10 ** arr[i]) * baknotestouse
    #print('res', res)
    allbanknotes -= baknotestouse
    if allbanknotes == 0:
      break
  print(res)