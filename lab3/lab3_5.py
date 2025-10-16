n = int(input())
a = list(map(int, input().split()))
p = int(input())

a = sorted(a)
ans = 0

def count(s):
    low = 0
    high = len(a)
    while low < high:
        mid = (low + high) // 2
        if a[mid] <= s:
            low = mid + 1
        else:
            high = mid
    return low, sum(a[0:low])

for _ in range(p):
    s = int(input())
    print(count(s)[0], count(s)[1])