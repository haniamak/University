t = int(input())

for _ in range(t):

  n = int(input())
  s = str(input())

  
  stack = []
  pos = {i:0 for i in range(n+1)} 
  res = 0

  for char in s:
    if char == "(":
      pos[len(stack)] = 1
      stack.append(char)
    else:
      res += pos[len(stack)] 
      pos[len(stack)] = 0
      stack.pop()

  res += pos[0]
  print(res)

      
