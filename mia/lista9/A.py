n, m = map(int, input().split())

students = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    students[a].append(b)
    students[b].append(a)

lentable = [0] * (n + 1)
for i in range(len(students)):
    lentable[i] = len(students[i])

group = 0
while lentable.count(1) > 0:
    removestudents = []
    for i in range(1, n + 1):
        if lentable[i] == 1:
            removestudents.append(i)
    for student in removestudents:
        for friend in students[student]:
            students[friend].remove(student)
            lentable[friend] -= 1
        students[student] = []
        lentable[student] = 0
    group += 1

print(group)
