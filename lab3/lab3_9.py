n, p = map(int, input().split())
a = list(map(int, input().split()))

a = sorted(a)
ans = 0

def count(s):
    low = 0
    high = max(a)
    c = 0

    while low < high:
        mid = (low + high) // 2
        c += (i + mid - 1) // mid
        if c <= s:
            low = mid + 1
        else:
            high = mid
    return low

print(count(p))