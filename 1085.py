x,y,w,h = map(int, input().split())

result = min(abs(x-0),abs(x-w),abs(y-0),abs(y-h))
print(result)
