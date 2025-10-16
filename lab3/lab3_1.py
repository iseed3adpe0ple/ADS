
t = int(input())
s = list(map(int, input().split()))
a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(a)]
snake = []
positions = []
for i in range(a):
    if i % 2 == 0:
        for j in range(b):
            snake.append(arr[i][j])
            positions.append((i, j))
    else:
        for j in range(b-1, -1, -1):
            snake.append(arr[i][j])
            positions.append((i, j))


for k in range(len(s)):
    low = 0
    high = len(snake)-1
    f = False
    while low <= high:
        h = (low + high) // 2

        if s[k] > snake[h]:
            high = h-1
        elif s[k] < snake[h]:
            low = h+1
        else:
            print(positions[h][0], positions[h][1])
            f = True
            break
    if not f:
        print('-1')