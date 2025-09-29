a = int(input())
b = [int(i) for i in input().split()]
k = int(input())
t = 0
f = abs(k - b[0])
for i in range(a):
    if abs(k - b[i]) < f:
        f = abs(k - b[i])
        t = i
print(t)