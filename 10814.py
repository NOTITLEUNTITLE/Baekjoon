N = int(input())

data = list()
for i in range(N):
    data.append(input().split())
data = sorted(data, key=lambda x: int(x[0]))

#print(data)
for d in data:
    print(" ".join(d))


