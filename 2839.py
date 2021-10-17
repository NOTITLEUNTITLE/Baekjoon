kg = int(input())
answer = 0

if kg == 4 or kg == 7:
    answer = -1

elif (kg%5 == 1):
    answer = 2 + (kg//5 - 1)

elif (kg%5 == 2):
    answer = 4 + (kg//5 - 2)

elif (kg%5 == 3):
    answer = 1 + kg//5

elif (kg%5 == 4):
    answer = 3 + (kg//5 - 1)

elif (kg%5 == 0):
    answer = kg//5

print(answer)
