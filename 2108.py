import sys
from collections import Counter

N = int(sys.stdin.readline())
data = list()
for i in range(N):
    data.append(int(sys.stdin.readline()))

print(round(sum(data)/N))
print(sorted(data)[N//2])
data.sort()
new_list = Counter(data).most_common(2)
if N == 1:
    print(data[0])
else:
    if new_list[0][1] == new_list[1][1]:
        print(new_list[1][0])
    else:
        print(new_list[0][0])
if N == 1:
    print(0)
else :
    print(max(data) - min(data))

