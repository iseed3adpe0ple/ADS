a = int(input())
b = [int(i) for i in input().split()]
for i in range(len(b)):
    if i % 2 == 0:
        print(b[i], end=" ")