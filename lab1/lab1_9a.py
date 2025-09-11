from collections import deque

n = int(input())
a = deque(input())

while 'S' in a and 'K' in a:
    current = a[0]
    a.rotate(-1)
    if current == 'S':
        a.remove('K')
    else:
        a.remove('S')

if 'S' in a:
    print("SAKAYANAGI")
else:
    print("KATSURAGI")
