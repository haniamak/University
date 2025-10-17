t = int(input())

for _ in range(t):
  l, r = map(int, input().split())
  mod2 = r // 2 - (l - 1) // 2
  mod3 = r // 3 - (l - 1) // 3
  mod5 = r // 5 - (l - 1) // 5
  mod7 = r // 7 - (l - 1) // 7
  mod2and3 = r // 6 - (l - 1) // 6
  mod2and5 = r // 10 - (l - 1) // 10
  mod2and7 = r // 14 - (l - 1) // 14
  mod3and5 = r // 15 - (l - 1) // 15
  mod3and7 = r // 21 - (l - 1) // 21
  mod5and7 = r // 35 - (l - 1) // 35
  mod2and3and5 = r // 30 - (l - 1) // 30
  mod2and3and7 = r // 42 - (l - 1) // 42
  mod2and5and7 = r // 70 - (l - 1) // 70
  mod3and5and7 = r // 105 - (l - 1) // 105
  mod2and3and5and7 = r // 210 - (l - 1) // 210
  res = (r - l + 1) - (mod2 + mod3 + mod5 + mod7) + (mod2and3 + mod2and5 + mod2and7 + mod3and5 + mod3and7 + mod5and7) - (mod2and3and5 + mod2and3and7 + mod2and5and7 + mod3and5and7) + mod2and3and5and7
  print(res)
