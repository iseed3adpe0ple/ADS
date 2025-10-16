# n, k = map(int, input().split())
# s = list(map(int, input().split()))
# m = max(s)
# while True:
#
#     a = 0
#     t = 0
#     for i in s:
#         if a + i > m:
#             t += 1
#             a = i
#         else:
#             a += i
#     if t > k-1:
#         m += 1
#         continue
#     else:
#         break
# print(m)

n, k = map(int, input().split())
s = list(map(int, input().split()))

low = max(s)
high = sum(s)

while low < high:
    mid = (low + high) // 2
    a = 0
    t = 1
    for i in s:
        if t > k:
            break
        if a + i > mid:
            t += 1
            a = i
        else:
            a += i
    if t > k:
        low = mid+1
    else:
        high = mid
print(low   )