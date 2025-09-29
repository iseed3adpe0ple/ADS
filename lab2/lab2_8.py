from collections import deque
a = deque()
s = input().split()
while s[0] != 'exit':
    if s[0] == 'add_front':
        a.appendleft(s[1])
        print('ok')
    elif s[0] == 'add_back':
        a.append(s[1])
        print('ok')
    elif s[0] == 'erase_front':
        if len(a) == 0:
            print('error')
        else:
            print(a.popleft())
    elif s[0] == 'erase_back':
        if len(a) == 0:
            print('error')
        else:
            print(a.pop())
    elif s[0] == 'front':
        if len(a) == 0:
            print('error')
        else:
            print(a[0])
    elif s[0] == 'back':
        if len(a) == 0:
            print('error')
        else:
            print(a[-1])
    elif s[0] == 'clear':
        a.clear()
        print("ok")
    s = input().split()

print('goodbye')