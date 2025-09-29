from collections import deque
t = input().split()
a = int(t[0])
b = int(t[1])
s = deque(input().split(" "))

s.rotate(-b)
for i in s:
    print(i, end=" ")
