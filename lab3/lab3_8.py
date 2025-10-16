import sys
input = sys.stdin.buffer.readline

n = int(input())
p = list(map(int, input().split()))
a = int(input())

low, high, target = 0, n - 1, -1
while low <= high:
    mid = (low + high) // 2
    if p[mid] >= a:
        target = mid
        high = mid - 1
    else:
        low = mid + 1
if target != -1 and p[target] == a:
    print("Yes")
else:
    print("No")