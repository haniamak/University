t = int(input())

for _ in range(t):

  n = int(input())

  s = str(0) + str(input())
  counter = 0

  if '0' not in s:
    counter = 1
  else: 
    for i in range(0, len(s) - 1):
      if s[i]!= s[i+1]:
        counter += 1
  
  
  print(counter)
