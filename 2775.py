t = int(input())
count = 1
result = []
for i in range(t):
    k = int(input())
    n = int(input())
    table = [[0 for j in range(n)] for i in range(k+1)]
    for row in range(k+1):
        for col in range(n):
            if row == 0:
                table[row][col] = count 
                count += 1
            else :
                table[row][col] = sum(table[row-1][:col+1])
    count = 1
    result.append((max(max(table))))

for answer in result:
    print(answer)
