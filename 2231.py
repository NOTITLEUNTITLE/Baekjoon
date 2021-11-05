# N = int(input())
# #자릿수
# de = len(str(N))
# start = N - (de * 9)
# print(de)
# print(start)
# print(sum(list(map(int, str(start)))))



# for i in range(start, N+1):
#   if i + sum(list(map(int, str(i)))) == N:
#     print(i)
#     break
#   if i == N:
#     print(0)
#     break

N = int(input())
for i in range(1, N+1):
  if i + sum(list(map(int, str(i)))) == N:
    print(i)
    break
  if i == N:
    print(0)
    break