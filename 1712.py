A, B, C = input().split()

A = int(A)
B = int(B)
C = int(C)

if B >= C:
    print(-1)
    quit()

temp = C - B
result = int(A / temp) + 1

print(result)