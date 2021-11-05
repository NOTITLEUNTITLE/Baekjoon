N = int(input())
data = list()
for i in range(N):
    data.append(list(map(int, input().split())))

data = sorted(data, key=lambda x: (x[1],x[0]))


for d in data:
    print(d[0],d[1])
