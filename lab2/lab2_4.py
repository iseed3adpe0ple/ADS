a = int(input())
b = [int(i) for i in input().split()]
s = []
b.sort(reverse=True)
f = 1
t = 1
for i in range(1, len(b)):
    if b[i] == b[i-1]:
        t += 1
    else:
        if t > f:
            s.clear()
            s.append(b[i-1])
            f = t
        elif t == f:
            s.append(b[i-1])
        t = 1

if t > f:
    s.clear()
    s.append(b[-1])
elif t == f:
    s.append(b[-1])

for i in s:
    print(i, end=" ")