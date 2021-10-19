import math


n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    length = y-x
    temp = length ** 0.5

    min_scope = math.floor(temp)
    max_scope = min_scope + 1
    # 17이라면
    if min_scope ** 2 + min_scope <= length:
        print(min_scope*2-1)
    elif min_scope ** 2 + min_scope >= length:
        print(min_scope*2+1)
    


    




