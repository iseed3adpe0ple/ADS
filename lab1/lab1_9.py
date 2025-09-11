n = int(input())
a = input()
b1 = 0
b2 = 0
while 'S' in a and 'K' in a:
    t = 0
    while b1 > 0 and a.find('K') != -1:
        for i in a:
            if i == 'K':
                h = a.find('K')
                a = a[:h] + a[h+1:]
                b1 -= 1
                break
    while b2 > 0 and a.find('S') != -1:
        for i in a:
            if i == 'S':
                h = a.find('S')
                a = a[:h] + a[h+1:]
                b2 -= 1
                break
    while t < len(a):
        if a[t] == "S":
            h = a.find("K", t+1)
            if h == -1:
                b1 += len(a) - t
            if h != -1:
                a = a[:h] + a[h+1:]
            t += 1
        elif a[t] == "K":
            h = a.find("S", t+1)
            if h == -1:
                b2 += len(a) - t
            if h != -1:
                a = a[:h] + a[h+1:]
            t += 1
        else:
            t += 1

if 'K' not in a:
    print("SAKAYANAGI")
else:
    print("KATSURAGI")
