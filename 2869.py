import math
num = list(map(int, input().split()))
data = num[0] - num[1]
print(math.ceil((num[2]-num[0]) / (num[0]-num[1]))+1)
