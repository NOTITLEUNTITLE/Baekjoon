

while True:
    line1, line2, line3 = map(int, input().split())
    if line1 == 0 and line2 == 0 and line3 == 0:
        break
    if line1 ** 2 == (line2 ** 2 + line3 ** 2):
        print("right")
    elif line2 ** 2 == (line1 ** 2 + line3 ** 2):
        print("right")
    elif line3 ** 2 == (line1 ** 2 + line2 ** 2):
        print("right")
    else:
        print("wrong")


