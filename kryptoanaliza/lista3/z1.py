import hashlib
import random

left_template = """<html>
<head>
<style type="text/css">
   p.a {{ font-style: italic; }}
</style>
<!-- NONCE: {nonce} -->
</head>
<body>
<p class="a">Jest bombowo!</p>
</body>
</html>
"""

right_template = """<html>
<head>
<style type="text/css">
   p.b {{ font-style: italic; }}
</style>
<!-- NONCE: {nonce} -->
</head>
<body>
<p class="b">Jest kiepsko!</p>
</body>
</html>
"""

def sha256_hex(s: str) -> str:
  return hashlib.sha256(s.encode('utf-8')).hexdigest()

def find_collision_24bit():
  seen = {}  # prefix -> (nonce, hash)
  while True:
    nonce_left = random.randint(0, 2**16)
    nonce_right = random.randint(0, 2**16)
    left = left_template.format(nonce=nonce_left)
    right = right_template.format(nonce=nonce_right)

    hash_left = sha256_hex(left)[:6]
    hash_right = sha256_hex(right)[:6]

    seen[hash_left] = (nonce_left, hash_left)
    if hash_right in seen and seen[hash_right][0] != nonce_right:
      return seen[hash_right], (nonce_right, hash_right), hash_right


found_left, found_right, prefix = find_collision_24bit()
print("Znaleziono kolizje: ")
print("Wspolny prefiks:", prefix)
print("Lewy dokument:")
print(f"Nonce: {found_left[0]}\nHash:  {found_left[1]}")
print("Prawy dokument:")
print(f"Nonce: {found_right[0]}\nHash:  {found_right[1]}")


with open("left_collision.html", "w", encoding="utf-8") as f:
    f.write(left_template.format(nonce=found_left[0]))
with open("right_collision.html", "w", encoding="utf-8") as f:
    f.write(right_template.format(nonce=found_right[0]))
