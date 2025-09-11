s = input()
while s != '':
    if len(s) == 1:
        print("NO")
        break
    i = 0
    while i < len(s)-1:
        if s[i] == s[i+1]:
            s = s[:i] + s[i+2:]
        i += 1
    if len(s) == 1:
        print("NO")
        break
    if len(s) == 0:
        break
    if s[0] == s[-1]:
        s = s[1:-1]
    elif s[0] == s[1]:
        s = s[2:]
    elif s[-1] == s[-2]:
        s = s[:-2]
    else:
        print("NO")
        break
if s == '':
    print("YES")