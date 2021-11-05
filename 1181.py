N = int(input())
data = list()
for i in range(N):
    data.append(input())

data = set(data)
data = sorted(data, key=lambda x: (len(x),x))

for i in data:
    print(i)
