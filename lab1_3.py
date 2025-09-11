import re

s = input().split()
s1 = s[0]
s2 = s[1]
a1 = ''
a2 = ''
for i in range(len(s1)):
    if s1[i] != "#":
        a1 += s1[i]
    else:
        a1 = a1[:len(a1)-1]
for i in range(len(s2)):
    if s2[i] != "#":
        a2 += s2[i]
    else:
        a2 = a2[:len(a2)-1]

if a1 == a2:
    print("Yes")
else:
    print("No")