import timeit
import math

def prime(x):
  i = range(2, math.floor(math.sqrt(x)) + 1)
  for divider in i:
    if x % divider == 0:
      return False
  return True

def pierwsze_imperatywna(n):
  res = []
  for i in range(2, n + 1):
    if prime(i):
      res.append(i)
  return res

def pierwsze_skladana(n):
  res = [i for i in range(2, n + 1) if prime(i)]
  return res

def pierwsze_funkcyjna(n):
  res = list(filter(prime, range(2, n + 1)))
  return res

#print(pierwsze_imperatywna(15))
#print(pierwsze_skladana(15))
#print(pierwsze_funkcyjna(15))


print("n \t\timperatywna \tskladana \tfunkcyjna")
for x in range(10, 100, 10): 
  skladana_time=timeit.timeit(lambda:pierwsze_skladana(x),number=1000)
  imperatywna_time=timeit.timeit(lambda:pierwsze_imperatywna(x),number=1000)
  funkcyjna_time=timeit.timeit(lambda:pierwsze_funkcyjna(x),number=1000)
  print(f"{x}:\t\t{skladana_time:.3f}\t\t{imperatywna_time:.3f}\t\t{funkcyjna_time:.3f}")