n = int(input())
for f in range(n):
    a = int(input())
    s = input().split()
    ans = []
    h = 0
    print(s[h], end=' ')
    f1 = True
    for i in range(1, len(s)):
        if s[i] != s[i-1] and f1:
            if s[i] == s[h]:
                for j in range(h, len(s)):
                    if s[j] != s[h]:
                        h = j
                        break
                ans.append(s[h])
            else:
                ans.append(s[h])
        elif s[i] != s[i-1] and not f1:
            h = i
            ans.append(s[h])
            f1 = True
        elif s[i] == s[i-1]:
            if s[i] == s[h]:
                ans.append('-1')
                f1 = False
            else:
                ans.append(s[h])

    for i in ans:
        print(i, end=' ')
    print()