import os
import math

def count_k(n):
  k = math.ceil(math.log2(n))
  return k

def generate_num(n):
  if n <= 1:
    return 0
  k = count_k(n)
  print('k:', k)
  while True:
    bits = [str(os.urandom(1)[0] & 1) for _ in range(k)]
    num = int(''.join(bits), 2)
    print('generated bits: ', bits, ' which is decimal: ', num)
    if num < n:
      return num

num = 20
numtable = list(range(0, num))
print('numtable: ', numtable) 

# k = count_k(num)
# print('k:', k, '\n')

for i in range(num - 1, 0, -1):
  j = generate_num(i+1)
  print(i, j)
  # while j > i:
  #   j = generate_num(num, k)
  numtable[i], numtable[j] = numtable[j], numtable[i]
  print('after swap: ', numtable)


reversed_numtable = numtable[::-1]
print('permutacja: ', reversed_numtable)
