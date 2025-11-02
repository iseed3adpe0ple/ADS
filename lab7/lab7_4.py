g = {
    "A+":4.0,"A":3.75,"B+":3.5,"B":3.0,
    "C+":2.5,"C":2.0,"D+":1.5,"D":1.0,"F":0
}

n = int(input())
arr = []

for i in range(n):
    line = input().split()
    last = line[0]
    first = line[1]
    k = int(line[2])
    s = 0
    c = 0
    j = 3
    for t in range(k):
        mark = line[j]
        cr = int(line[j+1])
        s += g[mark]*cr
        c += cr
        j += 2
    avg = s / c
    arr.append([last, first, avg])

arr.sort(key=lambda x:(x[2], x[0], x[1]))  # теперь по возрастанию GPA

for p in arr:
    print(p[0], p[1], f"{p[2]:.3f}")
