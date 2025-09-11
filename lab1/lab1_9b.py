from collections import deque

n = int(input())
a = deque(input())

qS = deque()
qK = deque()

t = 0
for i in a:
    if i == 'K':
        qK.append(t)
    else:
        qS.append(t)
    t += 1

while len(qS) >= 1 and len(qK) >= 1:
    if qS[0] < qK[0]:
        qK.popleft()
        qS.append(qS.popleft() + n+1)
    else:
        qS.popleft()
        qK.append(qK.popleft() + n+1)

if len(qS) >= 1:
    print("SAKAYANAGI")
else:
    print("KATSURAGI")
