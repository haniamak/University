def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def findGCD(array):
    res = array[0]
    for num in array[1:]:
        res = gcd(num, res)

        if res == 1:
            return 1
    return res

print(findGCD([3, 4, 6, 8, 10]))

def findLCM(array):
    lcm = array[0]
    for i in range(1, len(array)):
        lcm = (array[i] * lcm) // gcd(array[i], lcm)
    return lcm

print(findLCM([3, 4, 6, 8, 10]))
