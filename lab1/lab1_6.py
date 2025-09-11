import math
a = int(input())
i = 0
h = 1
while i < a:
    f = False
    h += 1
    if h == 2:
        i += 1
        continue
    elif h == 3:
        i += 1
        continue
    for j in range(2, int(math.sqrt(h))+1):
        if h % j == 0:
            f = True
            break
    if not f:
        i += 1
print(h)