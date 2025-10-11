tests = int(input())

for _ in range(tests):

  n = int(input())

  minnums = []
  secondminnums = []

  for _ in range(n):
    m = int(input())

    arr = list(map(int, input().split()))
    #print(arr)

    arr.sort()
    minnums.append(arr[0])
    secondminnums.append(arr[1])
  
  res = sum(secondminnums) - min(secondminnums) + min(minnums) 

  print(res)
