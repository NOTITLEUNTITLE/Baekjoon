import sys
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
temp = sorted(list(set(data)))

dic = {temp[i] : i for i in range(len(temp))}
for i in data:
    print(dic[i], end = ' ')