n = int(input())
schema = str(input())

starspositions = [i for i in range(n) if schema[i] == "*"]

if len(starspositions) < 5:
    print("no")
else:
    for i in range(len(starspositions)):
        for j in range(i + 1, len(starspositions)):
            jumps = 2
            distance = starspositions[j] - starspositions[i]
            currentpos = starspositions[j]

            while currentpos + distance in starspositions:
                currentpos += distance
                jumps += 1
                if jumps == 5:
                    print("yes")
                    exit(0)
    print("no")
