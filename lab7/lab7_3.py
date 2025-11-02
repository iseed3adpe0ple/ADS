n, m = map(int, input().split())
a = list(map(int, input().split())) if n > 0 else []
b = list(map(int, input().split())) if m > 0 else []
if not a or not b:
    print()
else:
    res = []
    for x in a:
        if x in b:
            res.append(x)
            b.remove(x)
    print(*sorted(res))
