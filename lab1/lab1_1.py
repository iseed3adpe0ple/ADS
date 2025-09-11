from collections import deque
answer = []
t = int(input())
for i in range(t):
    n = int(input())
    a = [int(j)+1 for j in range(n)]
    b = deque(a)
    q = 1
    while len(b) > 2:
        b.popleft()
        q+=1
    while q>=1:
        b.rotate(q)
        q-=1
        if(q != 0):
            b.appendleft(q)
    a = list(b)
    answer.append(a)
for i in answer:
    print(*i)

