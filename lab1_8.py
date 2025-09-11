import math
a = int(input())
if a == 1:
    print("NO")
    exit()
elif a == 2:
    print("YES")
    exit()
elif a == 3:
    print("YES")
    exit()
else:
    for i in range(2, int(math.sqrt(a))+1):
        if a % i == 0:
            print("NO")
            exit()
print("YES")