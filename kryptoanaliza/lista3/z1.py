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

def hash(s):
    m = hashlib.sha256()
    m.update(s.encode("utf-8"))
    return m.digest()


def find_collision_24bit():
  seen_left = {}  # prefix -> (nonce, hash)
  seen_right = {}  # prefix -> (nonce, hash)
  while True:
    nonce_left = random.randint(0, 2**13)
    nonce_right = random.randint(0, 2**13)
    left = left_template.format(nonce=nonce_left)
    right = right_template.format(nonce=nonce_right)

    hash_left = hash(left).hex()[:6]
    hash_right = hash(right).hex()[:6]

    seen_left[hash_left] = (nonce_left, hash_left)
    seen_right[hash_right] = (nonce_right, hash_right)
  
    if hash_left in seen_right and seen_right[hash_left][0] != nonce_left:
      return (nonce_left, hash_left), seen_right[hash_left], hash_left
    if hash_right in seen_left and seen_left[hash_right][0] != nonce_right:
      return seen_left[hash_right], (nonce_right, hash_right), hash_right


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
