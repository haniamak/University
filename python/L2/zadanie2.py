def sudan(n, x, y):
  if n == 0:
    return x + y
  if y == 0:
    return x
  else:
    return sudan(n-1, sudan(n, x, y-1), sudan(n, x, y-1) + y)


memo = {"0,0,0" : 0}

def sudan_memo(n, x, y):
  key = str(n) + "," + str(x) + "," + str(y)
  if key in memo:
    return memo[key]
  if n == 0:
    memo[key] = x + y
    return memo[key]
  if y == 0:
    memo[key] = x
    return memo[key]
  else:
    memo[key] = sudan_memo(n-1, sudan_memo(n, x, y-1), sudan_memo(n, x, y-1) + y)
    return memo[key]

#największe sensowne wywołanie tej funkcji w wersji bez spamiętywania:
print(sudan(3, 1, 1))
print(sudan(2, 1, 2))

#największe sensowne wywołanie tej funkcji ze spamiętywania:
print(sudan_memo(3, 1, 1))
print(sudan_memo(2, 5, 2))