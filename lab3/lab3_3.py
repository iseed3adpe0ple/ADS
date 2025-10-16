n, k = map(int, input().split())
a = list(map(int, input().split()))
a = sorted(a)

for _ in range(k):
    l1, r1, l2, r2 = map(int, input().split())

    if r1 < l2 or r2 < l1:

        # [l1, r1]
        low = 0
        high = len(a)
        while low < high:
            mid = (low + high) // 2
            if l1 > a[mid]:
                low = mid + 1
            else:
                high = mid
        mini1 = low
        low = 0
        high = len(a)
        while low < high:
            mid = (low + high) // 2
            if r1 >= a[mid]:
                low = mid + 1
            else:
                high = mid
        maxi1 = low

        # [l2, r2]
        low = 0
        high = len(a)
        while low < high:
            mid = (low + high) // 2
            if l2 > a[mid]:
                low = mid + 1
            else:
                high = mid
        mini2 = low
        low = 0
        high = len(a)
        while low < high:
            mid = (low + high) // 2
            if r2 >= a[mid]:
                low = mid + 1
            else:
                high = mid
        maxi2 = low

        print((maxi1 - mini1) + (maxi2 - mini2))

    else:
        left = min(l1, l2)
        right = max(r1, r2)

        low = 0
        high = len(a)
        while low < high:
            mid = (low + high) // 2
            if left > a[mid]:
                low = mid + 1
            else:
                high = mid
        mini = low
        low = 0
        high = len(a)
        while low < high:
            mid = (low + high) // 2
            if right >= a[mid]:
                low = mid + 1
            else:
                high = mid
        maxi = low

        print(maxi - mini)
