n, k = map(int, input().split())
p = [tuple(map(int, input().split())) for _ in range(n)]

def count(s):
    count = 0
    for x1, y1, x2, y2 in p:
        if x2 <= s and y2 <= s:
            count += 1
    return count

left = 0
right = 10**9 + 1
ans = 0
while left <= right:
    mid = (left + right) // 2
    if count(mid) >= k:
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)