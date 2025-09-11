from collections import deque

a = deque()
while True:
    n = input()
    if n == '!':
        exit()
    elif n == "":
        continue
    n = n.split()

    if n[0] == '+':
        a.appendleft(n[1])
    elif n[0] == '-':
        a.append(n[1])
    elif n[0] == '*':
        if len(a) >= 2:
            print(int(a[0]) + int(a[-1]))
            a.popleft()
            a.pop()


        elif len(a) == 1:
            print(int(a[0])*2)
            a.pop()
        elif len(a) == 0:
            print("error")

