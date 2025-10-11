from collections import deque

numberoftests = int(input())
for _ in range(numberoftests):
    n = int(input())
    a = [0] + list(map(int, input().split()))

    dp = [0] * (n + 1)
    q = [deque() for _ in range(n + 1)]

    for i in range(1, n + 1):
        x = a[i]
        dp[i] = dp[i - 1]
        q[x].append(i)

        if len(q[x]) > x:
            q[x].popleft()

        if len(q[x]) == x:
            dp[i] = max(dp[i], dp[q[x][0] - 1] + x)

    print(dp[n])