import hashlib
from itertools import combinations

isspace = [2, 3, 6, 8, 10, 13, 14, 15, 16, 17, 18, 20, 21]
alllines = list(range(1, 40))
freelines = [line for line in alllines if line not in isspace]
print(len(freelines))

def sha256_hex(s: str) -> str:
  return hashlib.sha256(s.encode('utf-8')).hexdigest()

with open("zad11.txt", "r") as f:
  lines = f.read().split("\n")

for i in range(6, len(freelines) + 1):
  print("dla i =", i)
  for comb in combinations(freelines, i):
    modifylines = lines.copy()
    for line in comb:
      modifylines[line - 1] += " "
    text = "\n".join(modifylines)
    hashtext = sha256_hex(text)
    if hashtext.startswith("000000"):
      print("Znaleziono kolizje przy ", i, " liniach")
      with open("res.txt", "w") as o:
        o.write(text)