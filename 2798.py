from itertools import combinations

N, M = map(int, input().split())
data = list(map(int, input().split()))
result = 0

# print(list(combinations(data, 3)))
data = list(combinations(data, 3))

for d in data:
  # print(sum(d))
  if sum(d) == M:
    print(M)
    exit()
  elif result < sum(d) and sum(d) < M:
    result = sum(d)
print(result)
