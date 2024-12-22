def longest_increasing_subsequence(arr):
    n = len(arr)
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_length = max(lis)
    if max_length >= 3:
        return True
    else:
        return


t = [1,5,0,4,1,3]
print(longest_increasing_subsequence(t))