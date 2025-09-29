b = int(input())
a = []
for i in range(b):
    a.append(int(input()))
c = int(input())
k = int(input())

a.insert(k, c)
for i in a:
    print(i, end=' ')