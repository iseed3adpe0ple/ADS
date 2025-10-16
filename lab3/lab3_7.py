import sys
input = sys.stdin.buffer.readline
write = sys.stdout.write

n, m = map(int, input().split())
p = list(map(int, input().split()))

pref = [0] * n
s = 0
for i in range(n):
    s += p[i]
    pref[i] = s

def binary_search(b):
    low, high, target = 0, n - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if pref[mid] >= b:
            target = mid
            high = mid - 1
        else:
            low = mid + 1
    return target + 1

out = []
append_out = out.append

for _ in range(m):
    b = int(input())
    append_out(str(binary_search(b)))

write("\n".join(out))
