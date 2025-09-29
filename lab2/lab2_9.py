from collections import defaultdict

n = int(input())
for k in range(n):
    ans = []
    a = int(input())
    s = input().split()
    d = []
    freq = defaultdict(int)

    d.append(s[0])
    freq[s[0]] += 1
    d1 = 0
    print(s[0], end=' ')

    for i in range(1, a):
        freq[s[i]] += 1

        if s[i] not in d:
            d.append(s[i])

        while d1 < len(d) and freq[d[d1]] > 1:
            d1 += 1

        if d1 < len(d):
            ans.append(d[d1])
        else:
            ans.append('-1')

    for i in ans:
        print(i, end=' ')
    print()
