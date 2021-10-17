n = int(input())
num = [[] for i in range(n)]
for i in range(n):
   num[i] = list(map(int, input().split()))

for i in range(n):
   #몇 호인지를 나타내는 값
   # print(num[i][2] // num[i][0])
   room = num[i][2] // num[i][0]
   #몇 층인지를 나타내는 값
   # print(num[i][2] % num[i][0])
   floor = num[i][2] % num[i][0]
   if floor == 0:
      print(f"{num[i][0]*100 + room}")
   else :
      print(f"{floor*100 + room+1}")
