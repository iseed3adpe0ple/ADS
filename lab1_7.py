import math
a = int(input())

i = 0
k = 0
h = 1
f1 = False
while k < a:
    f1 = False
    f = False
    h += 1
    if h == 2:
        i += 1
        f1 = True
        f = True
    elif h == 3:
        i += 1
        f1 = True
        f = True
    else:
        for j in range(2, int(math.sqrt(h)) + 1):
            if h % j == 0:
                f = True
                break
    if not f:
        i += 1
        f1 = True

    if f1:
        f = False
        if i == 1:
            continue
        elif i == 2:
            k += 1
            continue
        elif i == 3:
            k += 1
            continue
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                f = True
                break
        if not f:
            k += 1

print(h)