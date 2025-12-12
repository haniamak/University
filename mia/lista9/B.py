n = int(input())
a = list(map(int, input().split()))

a.insert(0, 0)
a.insert(0, 0)


def dfs(v):
    global answer
    if v >= leaves:
        return 0
    left = dfs(2 * v) + a[2 * v]
    right = dfs(2 * v + 1) + a[2 * v + 1]
    answer += abs(left - right)
    return max(left, right)


leaves = 2**n
nodes = 2 ** (n + 1)

answer = 0
dfs(1)
print(answer)
