a = input().split()
a = [int(i) for i in a]
b = input().split()
b = [int(i) for i in b]

t = -1
while True:
    t += 1
    if len(a) == 0:
        print("Nursik", t)
        break
    elif len(b) == 0:
        print("Boris", t)
        break
    elif t>1000000:
        print("blin nichya")
        break
    if a[0] == 0 and b[0] == 9:
        a.append(a[0])
        a.append(b[0])
        b.pop(0)
        a.pop(0)
    elif a[0] == 9 and b[0] == 0:
        b.append(a[0])
        b.append(b[0])
        a.pop(0)
        b.pop(0)
    elif a[0] > b[0]:
        a.append(a[0])
        a.append(b[0])
        b.pop(0)
        a.pop(0)
    else:
        b.append(a[0])
        b.append(b[0])
        a.pop(0)
        b.pop(0)

