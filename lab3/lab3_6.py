n, f = map(int, input().split())
a = list(map(int, input().split()))

low = 1
high = max(a)
ans = high

while low <= high:
    mid = (low + high) // 2
    count = 0
    for i in a:
        count += (i + mid - 1) // mid  # ceil(i / mid)

    if count <= f:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)
