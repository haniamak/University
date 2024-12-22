import random
import math

def wyliczPi(maxRoznica):

  rzuty = 1000
  bok = 1
  ltwo = 0
  cltwt = 0

  for i in range(rzuty):
    x = random.uniform(-bok, bok)
    y = random.uniform(-bok, bok)
    odl = math.sqrt(x * x + y * y)

    if odl <= bok:
      ltwo += 1
    cltwt += 1

    przyblizenie = (4 * ltwo) / cltwt
    print(f"przybliżenie po rzucie {i + 1}: {przyblizenie}")

    if abs(przyblizenie - math.pi) < maxRoznica:
      print("koniec programu")
      break


wyliczPi(0.001)
