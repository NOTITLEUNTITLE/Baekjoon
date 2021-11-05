N = int(input())
x = list()
y = list()
for _ in range(N):
    temp_x, temp_y = map(int, input().split())
    x.append(temp_x)
    y.append(temp_y)

for i in range(N):
    rank = 0
    for j in range(N):
        if x[i] < x[j] and y[i] < y[j]:
            rank += 1
    print(rank + 1)


