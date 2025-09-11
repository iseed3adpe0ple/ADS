n = int(input())
a = []
answer = []
a = input().split()
a = [int(a[i]) for i in range(n)]
for i in range(n):
    if i == 0:
        answer.append(-1)
    else:
        k = i-1
        f = False
        while k >= 0:
            if a[k] <= a[i]:
                answer.append(a[k])
                f = True
                break
            k -= 1
        if f == False:
            answer.append(-1)
print(*answer)