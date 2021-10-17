num = int(input())
start = 1
linear = 6
minnum_pass_room = 1
if num == 1:
    print(1)
else:
    while True:
        start = start + linear
        minnum_pass_room += 1
        if num <= start:
            print(minnum_pass_room)
            break
        linear += 6
