n, m = map(int, input().split())
a = []

for i in range(n):
    row = list(map(int, input().split()))
    a.append(row)

def key_func(row):
    return (-sum(row), row)

a.sort(key=key_func)

for r in a:
    print(*r, end=' \n')
