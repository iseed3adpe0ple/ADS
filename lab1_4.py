s = input()
while s != '':
    if len(s) == 1:
        print("NO")
        break
    elif len(s) == 0:
        print("YES")
        break
    if s[0] == s[-1]:
        s = s[1:-1]
    elif s[0] == s[1]:
        s = s[2:]
    elif s[-1] == s[-2]:
        s = s[:-2]
    else:
        f = True
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                f = False
                s = s[:i] + s[i+2:]
                break
        if f:
            print("NO")
            break
if s == '':
    print("YES")