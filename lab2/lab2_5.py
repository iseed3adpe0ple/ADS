a = int(input())
b = []
i = 0
while i < a:
    b.append(input())
    if i == 0:
        i+=1
        continue
    if b[i-1] == b[i]:
        b.pop()
        a -= 1
        continue
    i+=1
b.reverse()
print("All in all:", len(b))
print("Students:")
for i in b:
    print(i)