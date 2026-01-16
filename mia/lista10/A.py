n, d = map(int, input().split())
p = list(map(int, input().split()))
p.sort()
i = 0
j = n - 1
counter = 0

while i <= j:
    max_power = p[j]
    needed = d // max_power + 1

    if j - i + 1 >= needed:
        counter += 1
        i += needed - 1
        j -= 1
    else:
        break

print(counter)
